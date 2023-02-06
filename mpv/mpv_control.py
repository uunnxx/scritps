#!/bin/env python

import os
import sys
from python_mpv_jsonipc import MPV


socket_path = os.path.expanduser("~/.mpv/socket")
mpv = MPV(start_mpv=False, ipc_socket=socket_path)


def mpv_control():
    given = sys.argv[1:]
    match given:
        case ['pause']:
            mpv.command('set', 'pause', 'yes')
        case ['play']:
            mpv.command('set', 'pause', 'no')
        case ['next']:
            mpv.command('playlist_next')
        case ['prev']:
            mpv.command('playlist_prev')


if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print("""Usage: pause, play, next, prev """)
        mpv.terminate()
        sys.exit(1)

    mpv_control()
    mpv.terminate()
