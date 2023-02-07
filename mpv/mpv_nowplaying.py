#!/bin/env python

import os
import re
import subprocess
import sys
from python_mpv_jsonipc import MPV


# Run mpv:
# mpv --input-ipc-server=/home/<user>/.mpv/socket
socket_path = os.path.expanduser("~/.mpv/socket")

mpv = MPV(start_mpv=False, ipc_socket=socket_path)
youtube_id = re.compile("( \[?[a-zA-Z0-9\-\_]{11}]?.+)")
coub_id = re.compile("( \[?[a-zA-Z0-9\-\_]{6}]?.+)")


@mpv.property_observer('filename')
def broadcast_filename(name='', data=''):
    mpv.pause = False
    filename = re.sub(youtube_id, '', data)
    filename = re.sub(coub_id, '', data)
    playlist_current = mpv.playlist_current_pos+1
    playlist_count = mpv.playlist_count
    args = [
        'dunstify',
        '-r', '9999',
        '-u', 'normal',
        f'NOW PLAYING: [ {playlist_current} of {playlist_count} ]',
        f'{filename}'
    ]
    subprocess.run(args)


if __name__ == '__main__':
    broadcast_filename()
