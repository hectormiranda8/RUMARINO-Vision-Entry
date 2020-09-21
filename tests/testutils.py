import sys
import os
sys.path.append('./src')

import unittest

from fileutils import files2list, list2file

class TestUtils(unittest.TestCase):

    def test_file_reading(self):
        self.assertEqual(files2list("./src", ".py"), ["cvutils.py", "darknetutils.py", "fileutils.py"], "Must return the files present in the src folder.")

    def test_file_writing(self):
        filearr = files2list("./src", ".py")

        list2file("test.txt", filearr)

        with open("test.txt", 'r') as file:
            for i in file:
                self.assertEqual(i[:-1], filearr.pop(0), "Text file output must be the same.")

        os.remove("test.txt")

if __name__ == '__main__':
    unittest.main()