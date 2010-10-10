#! ../ve/bin/env python

import serial
import glob

def scan():
    return glob.glob('/dev/ttyS*') + glob.glob('/dev/ttyUSB*')

if __name__=='__main__':
    print("ports:")
    for name in scan():
        print(name)
