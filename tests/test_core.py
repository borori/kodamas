# coding: utf-8

import unittest
from kodamas import core
from mock import MagicMock as Mock
import os
import shlex

class TestCore(unittest.TestCase):
    def test_main_oneshot(self):
        ''' if oneshot is True, main functioin break 'loop'. '''
        os.read = Mock(return_value=b'x01x00x00x00x08x00x00x00x00x00x00x00x10x00x00x00') 
        shell = shlex.split('echo "hello"')	
        core.main('/tmp/sample',shell, [], True)
        


if __name__ == '__main__':
    unittest.main() 
