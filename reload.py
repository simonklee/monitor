#!ve/bin/python

import subprocess

def reload():
    '''
    A hack to reload the uwsgi worker. Think uwsgi 9.5 will
    make this obsolete.
    '''
    with open('pid.txt') as fp:
        pid = fp.read().rstrip()
        print(pid)
        subprocess.call(['sudo', 'kill' , pid])
    fp.close()

reload()
