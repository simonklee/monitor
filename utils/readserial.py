#! ../ve/bin/env python

import re
import os
import sys
import time
import serial
import glob
import threading
import logging
import datetime

proj = os.path.dirname(os.getcwd())
sys.path.append(proj)
sys.path.append(os.path.dirname(proj))
sys.path.append(os.path.join((proj, 've/')))

from django.core.management import setup_environ
from monitor import settings
setup_environ(settings)

from monitor.apps.mon.models import Record

logging.basicConfig(level=logging.DEBUG)

EOF = ';'
LF = '\n'
DEL = ','

COMMIT = False


class Monitor(object):

    def __init__(self, serials=None, *args, **kwargs):
        self.baud = kwargs.get('baud', 115200)
        self.timeout = kwargs.get('timeout', 0)
        self.serials = serials
        self._tty_cache_of = 4
        self._tty_cache_timeout = None
        self._tty_cache = None

    def tty_list(self, **kwargs):
        try:
            return [serial.Serial(port, self.baud, timeout=self.timeout) for port in self.tty_names()]
        except IOError:
            if kwargs.get('rec', True):
                self._tty_cache_timeout = 0
                return self.tty_list(rec=False)
            else:
                raise

    def tty_names(self):
        return self.serials if self.serials else self.tty_scan()

    def tty_scan(self):
        if self._tty_cache is None or self._cache_timeout():
            self._tty_cache = glob.glob('/dev/ttyUSB*')
            self._tty_cache_timeout = self._timestamp() + self._tty_cache_of

        return self._tty_cache

    def _cache_timeout(self):
        return self._tty_cache_timeout is None or self._tty_cache_timeout < self._timestamp()

    def _timestamp(self):
        return time.mktime(datetime.datetime.now().timetuple())

    def run(self):
        tmp_names = self.tty_names()
        logging.info("Starting ... \nlistening on %s", tmp_names)

        while(1):
            res = list()
            for tty in self.tty_list():
                n = int(tty.inWaiting())
                if n > 0:
                    s = tty.read(n)
                    res.append(s)
                    if res[-1][-1] == EOF:
                        data = ''.join(res)
                        interp = Interpreter(data[:-1], commit=COMMIT)
                        interp.start()
                        res = list()
                        # logging.debug(data)

            main = threading.currentThread()
            for t in threading.enumerate():
                if t == main:
                    continue
                logging.debug(t.getName())

            if tmp_names != self.tty_names():
                tmp_names = self.tty_names()
                logging.debug("now listening on %s", tmp_names)
            time.sleep(0.1)


class Interpreter(threading.Thread):

    def __init__(self, data, commit=True):
        threading.Thread.__init__(self)
        self.data = data
        self._data_fields_abbr = Record.data_fields_abbr()
        self.commit = commit

    def run(self):
        r = Record(**self.interpret())
        if self.commit:
            r.save()
        else:
            r.created = datetime.datetime.now()
            logging.info("Record(created: %s, current: %s, volt: %s, temp: %s, light: %s)" %
                                (r.created, r.current, r.volt, r.temp, r.light))

    def interpret(self):
        values = [d for d in self.data.split(DEL)]
        pairs = dict()

        for v in values:
            m = re.match(r'[a-zA-Z]+', v)
            if m is None:
                continue

            k = v[m.start():m.end()]
            try:
                k = self._data_fields_abbr[k.lower()]
            except KeyError:
                logging.debug("%s invalid key" % k)
                continue

            pairs[k] = v[m.end():]
        logging.debug("%s" % pairs)

        self.data_struct = pairs
        return pairs

if __name__=='__main__':
    while(1):
        mon = Monitor()
        mon.run()
