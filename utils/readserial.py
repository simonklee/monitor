#! ../ve/bin/env python

import os
import sys
import time
import serial
import glob

proj = os.path.dirname(os.getcwd())
sys.path.append(proj)
sys.path.append(os.path.dirname(proj))
sys.path.append(os.path.join((proj, 've/')))

from django.core.management import setup_environ
from monitor import settings
setup_environ(settings)

from monitor.apps.mon.models import Record

class Monitor(object):

    def __init__(self, serials=None, *args, **kwargs):
        self.baud = kwargs.get('baud', 115200)
        self.timeout = kwargs.get('timeout', 0)

        tty_names = serials if serials else self.tty_scan()
        self.tty_list = [serial.Serial(port, self.baud, timeout=self.timeout)
                    for port in tty_names]

    def tty_scan(self):
        return glob.glob('/dev/ttyUSB*')

    def run(self):
        while(1):
            for tty in self.tty_list:
                n = int(tty.inWaiting())
                if n > 0:
                    print(tty.portstr, tty.read(n))
            time.sleep(0.1)

if __name__=='__main__':
    mon = Monitor()
    mon.run()
