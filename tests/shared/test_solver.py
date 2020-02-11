import unittest

from boggle.shared.solver import BoggleDictionary
from boggle.shared.solver import BoggleSolver

class TestBoggleSolver(unittest.TestCase):
    """Boggle game solver test driver."""

    test_board = \
        'catx' \
        'xxnx' \
        'xxua' \
        'xxxx'

    def setUp(self):
        self.dictionary = BoggleDictionary()
        for w in ('ant', 'aunt', 'cat', 'zoo'):
            self.dictionary.add(w)

    def test_index(self):
        solver = BoggleSolver(self.dictionary)
        solver.build_index(self.test_board)
        got = solver.index
        expected = {
            'a': [1, 11],
            'b': [],
            'c': [0],
            'd': [],
            'e': [],
            'f': [],
            'g': [],
            'h': [],
            'i': [],
            'j': [],
            'k': [],
            'l': [],
            'm': [],
            'n': [6],
            'o': [],
            'p': [],
            'q': [],
            'r': [],
            's': [],
            't': [2],
            'u': [10],
            'v': [],
            'w': [],
            'x': [3, 4, 5, 7, 8, 9, 12, 13, 14, 15],
            'y': [],
            'z': [],
        }
        self.assertEqual(got, expected)

    def test_find_words(self):
        solver = BoggleSolver(self.dictionary)
        solver.build_index(self.test_board)
        got = solver.find_word('cat')
        expected = [0, 1, 2]
        self.assertEqual(got, expected)

    def test_solve(self):
        solver = BoggleSolver(self.dictionary)
        solver.solve(self.test_board)
        got = solver.solution
        expected = {
            'ant': (1, 6, 2),
            'aunt': (11, 10, 6, 2),
            'cat': (0, 1, 2),
        }
        self.assertEqual(got, expected)

if __name__ == '__main__':
    unittest.main()
