import os
import tempfile
import unittest

from boggle.shared.solver import BoggleDictionary

class TestBoggleDictionary(unittest.TestCase):
    """Boggle game dictionary test driver."""

    def setUp(self):
         f = tempfile.NamedTemporaryFile(delete=False)
         for w in ('ant', 'aunt', 'cat', 'ZOO', "it's"):
             f.write(bytes(w+'\n', 'ascii'))
         f.close()
         self.testfile = f.name

    def tearDown(self):
        os.remove(self.testfile)

    def test_read(self):
        d = BoggleDictionary()
        d.read(self.testfile)
        self.assertEqual(len(d.words), 4)
        self.assertTrue('ant' in d.words)
        self.assertTrue('aunt' in d.words)
        self.assertTrue('cat' in d.words)
        self.assertTrue('zoo' in d.words)


if __name__ == '__main__':
    unittest.main()
