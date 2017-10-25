# coding: utf-8

import ctypes
import ctypes.util
import os
import struct
import subprocess
import sys
import time
from kodamas import (
    INOTIFY_EVENT_PREFIX_LEN,
    INOTIFY_EVENT_MAX_LEN,
    IN_CLOSE_WRITE
)

def main(monitored, shell, exclude, oneshot=False):
    ''' Initialize inotify and watching loop '''
    # Inotify Settings
    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    inotify_fd = libc.inotify_init()
    file_name = monitored
    wd = libc.inotify_add_watch(
        inotify_fd,
        monitored.encode('utf-8'),
        IN_CLOSE_WRITE
    )
    try:
        while True:
            raw = os.read(inotify_fd, INOTIFY_EVENT_MAX_LEN)
            # struct.unpack return tuples below
            # (wd, mask, cookie, len)
            inotify_event = struct.unpack("i3I", raw[:INOTIFY_EVENT_PREFIX_LEN])
            if wd == int(inotify_event[0]):
                if int(inotify_event[3]) > 0:
                    raw_file_name = raw[
                        INOTIFY_EVENT_PREFIX_LEN:INOTIFY_EVENT_PREFIX_LEN +
                        inotify_event[3]
                    ]
                    file_name = raw_file_name.decode('utf-8').rstrip('\x00')
                    _, ext = os.path.splitext(file_name)
                    if ext in exclude:
                        continue
                print(
                    "\033[42m====\033[0m File Updated: %s @ %s \033[42m====\033[0m" %
                    (file_name, time.ctime())
                )
                subprocess.call(shell) # python 2.x 3.x compatible
            if oneshot:
                break
    except Exception:
        print(sys.exc_info())
