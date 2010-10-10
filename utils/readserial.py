#! ../ve/bin/env python

import time
import serial
import glob

def scan():
    return glob.glob('/dev/ttyUSB*')

def serials():
    return [serial.Serial(name, 115200, timeout=0) for name in scan()]

if __name__=='__main__':
    serial_list = serials()
    while(1):
        for tty in serial_list:
            n = int(tty.inWaiting())
            if n > 0:
                print(tty.portstr, tty.read(n))
        time.sleep(0.1)

