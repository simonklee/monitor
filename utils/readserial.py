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

logging.basicConfig(level=logging.INFO)

EOF = ';'
LF = '\n'
DEL = ','

COMMIT = False


class Monitor(object):

    def __init__(self, serials=None, *args, **kwargs):
        self.baud = kwargs.get('baud', 115200)
        self.timeout = kwargs.get('timeout', 0)
        self.serials = serials

    def tty_list(self):
        return [serial.Serial(port, self.baud, timeout=self.timeout) for port in self.tty_names()]

    def tty_names(self):
        return self.serials if self.serials else self.tty_scan()

    def tty_scan(self):
        return glob.glob('/dev/ttyUSB*')

    def run(self):
        logging.debug("listening on %s", self.tty_names())

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
        try:
            mon = Monitor()
            mon.run()
        except IOError:
            continue
