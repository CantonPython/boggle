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

    def _build_index(self, board):
        """Generate the index table for find_word."""
        self.index = {}
        for letter in string.ascii_lowercase:
            self.index[letter] = []
        for i,letter in enumerate(board):
            self.index[letter].append(i)

    def find_word(self, word):
        """Find the word on the board if it exists."""
        first = word[0]
        rest = word[1:]
        for i in self.index[first]:
            found = self._find_subword([i], rest)
            if found:
                return found
        return None

    def _find_subword(self, path, word):
        """Find the remaining letters of a word on the board."""
        if not word:
            return path
        first = word[0]
        rest = word[1:]
        tail = path[-1]
        adjacent = ADJACENT[tail]
        for i in self.index[first]:
            if i in adjacent and i not in path:
                found = self._find_subword(path+[i], rest)
                if found:
                    return found
        return None

    def solve(self, board):
        """Find all the words on the board."""
        self._build_index(board)
        self.solution = {}
        for word in self.dictionary:
            word = word.strip()
            path = self.find_word(word)
            if path:
                self.solution[word] = tuple(path)
        return self.solution

    def found(self):
        return list(self.solution.keys())

    def path_found(self, word):
        return self.solution[word]

def main():
    """Test driver for the boggle game solver."""
    boggle = BoggleSolver('boggle_words.txt')

    board = 'bpsrtsbevdjwcesy'
    boggle.solve(board)

    print('board', board)
    for word in boggle.found():
        print(word, boggle.path_found(word))

if __name__ == '__main__':
    main()
