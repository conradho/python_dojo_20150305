#/usr/bin/env python3.4

from collections import namedtuple
import unittest
import tempfile
import os

from cut_blank_lines import cut_blank_lines

TempFileTuple = namedtuple('TemporaryFile', ['file_descriptor', 'path'])

class TestCutBlankLines(unittest.TestCase):

    def setUp(self):
        self.sample_script = "print('hello')\n"
        self.temp_file = TempFileTuple(*tempfile.mkstemp())
        with os.fdopen(self.temp_file.file_descriptor, 'w') as opened_file:
            opened_file.write(self.sample_script)
            opened_file.write('\n\n\n')
            # this also closes the whole file; don't need to os.close it


    def test_blank_line_gets_cut(self):
        cut_blank_lines(self.temp_file.path)
        with open(self.temp_file.path, 'r') as test_file:
            self.assertEqual(test_file.read(), self.sample_script)
