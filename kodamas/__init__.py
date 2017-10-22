# coding: utf-8
'''setting inotify params'''

import struct
import os

# Inotify Events
IN_CLOSE_WRITE = 0x00000008
IN_ONESHOT = 0x80000000

# Define Length Limits
INOTIFY_EVENT_PREFIX_LEN = struct.Struct("i3I").size
NAME_MAX = os.pathconf('/', 'PC_NAME_MAX')
INOTIFY_EVENT_MAX_LEN = INOTIFY_EVENT_PREFIX_LEN + NAME_MAX + 1
