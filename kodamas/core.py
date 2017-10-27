# coding: utf-8

import ctypes
import ctypes.util
import os
import struct
import subprocess
import time
from kodamas import (
    INOTIFY_EVENT_PREFIX_LEN,
    INOTIFY_EVENT_MAX_LEN,
    IN_CLOSE_WRITE
)

def get_inotify_event_prefix(raw):
    ''' (bytes) -> list
    Extract inotify_event header from the bytes.
    struct.unpack return tuples below
    (wd, mask, cookie, len)
    '''
    return struct.unpack("i3I", raw[:INOTIFY_EVENT_PREFIX_LEN])

def get_file_name(raw, name_length):
    ''' (bytes, int) -> str
    Extract the file name from the bytes.
    '''
    return raw[
        INOTIFY_EVENT_PREFIX_LEN : INOTIFY_EVENT_PREFIX_LEN +
        name_length
    ].decode('utf-8').rstrip('\x00')

def is_target_extension(extension, extensions):
    ''' (list of str, str) -> boolean
    check this extension include the extensions.
    '''
    if not extensions:
        return True
    return bool(extension.lstrip('.') in extensions)

def main(monitored, shell, extensions):
    ''' (str, list of str, list of str, boolean) -> NoneType
    Initialize inotify and watching loop
    '''
    # Inotify Settings
    libc = ctypes.CDLL(ctypes.util.find_library("c"))
    inotify_fd = libc.inotify_init()
    file_name = monitored
    libc.inotify_add_watch(
        inotify_fd,
        monitored.encode('utf-8'),
        IN_CLOSE_WRITE
    )

    while True:
        raw = os.read(inotify_fd, INOTIFY_EVENT_MAX_LEN)
        inotify_event_prefix = get_inotify_event_prefix(raw)
        if int(inotify_event_prefix[3]) > 0:
            file_name = get_file_name(raw, inotify_event_prefix[3])
            _, extension = os.path.splitext(file_name)
            if is_target_extension(extension, extensions):
                print(
                    "\033[42m===\033[0m File Updated: %s @ %s \033[42m===\033[0m" %
                    (file_name, time.ctime())
                )
                subprocess.call(shell) # python 2.x 3.x compatible
