import string


# Adjacency table for a 4 x 4 board.
ADJACENT = {
    0: (1, 4, 5),
    1: (0, 2, 4, 5, 6),
    2: (1, 3, 5, 6, 7),
    3: (2, 6, 7),
    4: (0, 1, 5, 8, 9),
    5: (0, 1, 2, 4, 6, 8, 9, 10),
    6: (1, 2, 3, 5, 7, 9, 10, 11),
    7: (2, 3, 6, 10, 11),
    8: (4, 5, 9, 12, 13),
    9: (4, 5, 6, 8, 10, 12, 13, 14),
    10: (5, 6, 7, 9, 11, 13, 14, 15),
    11: (6, 7, 10, 14, 15),
    12: (8, 9, 13),
    13: (8, 9, 10, 12, 14),
    14: (9, 10, 11, 13, 15),
    15: (10, 11, 14),
}

class BoggleSolver:

    def __init__(self, filename='words.txt'):
        self.dictionary = []
        with open(filename) as f:
            for word in f:
                self.dictionary.append(word.strip())

    # TODO!
    def solve(self, board):
        pass

    def found(self):
        pass

def main():
    """Test driver for the boggle game solver."""
    boggle = BoggleSolver('boggle_words.txt')

    board = 'bpsrtsbevdjwcesy'
    boggle.solve(board)

    found = boggle.found()
    print('board', board, 'found', found)

if __name__ == '__main__':
    main()
