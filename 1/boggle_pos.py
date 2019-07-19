
# Helper functions to convert between row,col and index.

ROWS = 4
COLS = 4

def pos2index(row, col):
    return (row * ROWS) + col

def index2pos(i):
    row = i // ROWS
    col = i % ROWS
    return (row,col)

def in_bounds(row, col):
    return (0 <= row < ROWS) and (0 <= col < COLS)

def _test():
    print('row,col to index')
    for row in range(ROWS):
        for col in range(COLS):
            i = pos2index(row, col)
            print('{0}: ({1}, {2})'.format(i, row, col))

    print('index to row,col')
    for i in range(16):
        row,col = index2pos(i)
        print('{0}: ({1}, {2})'.format(i, row, col))

if __name__ == '__main__':
    _test()
