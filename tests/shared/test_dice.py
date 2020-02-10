
import unittest
import random
from boggle.shared.dice import BoggleDice

class TestBoggleDice(unittest.TestCase):

    def test_shake(self):
        random.seed(0)
        dice = BoggleDice()
        letters = dice.shake()
        self.assertEqual(letters, 'ibeomrsvkleyepio')

if __name__ == '__main__':
    unittest.main()
