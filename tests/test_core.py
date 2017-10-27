# coding: utf-8

import unittest
from kodamas import core

class TestCore(unittest.TestCase):

    def test_is_target_extension(self):
        ''' is_target_extension should return
            - true file extension include extensions(list)
            - false file extension not include extensions(list)
            and strip `.` from `extension verbs` while comparing
        '''
        self.assertTrue(core.is_target_extension('txt', ['txt', 'py']))
        self.assertTrue(core.is_target_extension('.txt', ['txt', 'py']))
        self.assertTrue(core.is_target_extension('txt', []))
        self.assertTrue(core.is_target_extension('', []))
        self.assertFalse(core.is_target_extension('txt', ['rb', 'py']))
        self.assertFalse(core.is_target_extension('', ['rb', 'py']))

    def test_get_inotify_event_prefix(self):
        ''' get_inotify_event_prefix should extract inotify_event_prefix from bytes '''
        bts1 = b'\x01' + (b'\x00' * 3) + b'\x08' + (b'\x00' * 3) + \
            (b'\x00' * 4) + b'\x10' + (b'\x00' * 3) + b'sample' + (b'\x00' * 10)
        self.assertEqual((1, 8, 0, 16), core.get_inotify_event_prefix(bts1))

    def test_get_file_name(self):
        ''' get_file_name should extract file name from bytes '''
        bts1 = b'\x01' + (b'\x00' * 3) + b'\x08' + (b'\x00' * 3) + \
            (b'\x00' * 4) + b'\x10' + (b'\x00' * 3) + b'sample' + (b'\x00' * 10)
        self.assertEqual('sample', core.get_file_name(bts1, 16))

if __name__ == '__main__':
    unittest.main()
