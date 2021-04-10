import random

HEIGHT = 100
WIDTH = 100


def randomize(grid, width, height):
    for i in range(0, height):
        for j in range(0, width):
            grid[i][j] = random.randint(0, 1)


GRID_MODEL = [0] * HEIGHT
NEXT_GRID_MODEL = [0] * HEIGHT
for i in range(HEIGHT):
    GRID_MODEL[i] = [0] * WIDTH
    NEXT_GRID_MODEL[i] = [0] * WIDTH


def next_gen():
    global GRID_MODEL, NEXT_GRID_MODEL

    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            cell = 0
            print("Checking Cell {} {}".format(i, j))
            count = count_neighbors(GRID_MODEL, i, j)

            if GRID_MODEL[i][j] == 0:
                if count == 3:
                    cell = 1
            elif GRID_MODEL[i][j] == 1:
                if count == 2 or count == 3:
                    cell = 1
            NEXT_GRID_MODEL[i][j] = cell
            print("New value is {}".format(NEXT_GRID_MODEL[i][j]))

    GRID_MODEL, NEXT_GRID_MODEL = NEXT_GRID_MODEL, GRID_MODEL


def count_neighbors(grid, row, col):

    count = 0
    if row - 1 >= 0:
        count += grid[row - 1][col]
    if (row - 1 >= 0) and (col - 1 >= 0):
        count += grid[row - 1][col - 1]
    if (row - 1 >= 0) and (col + 1 < WIDTH):
        count += grid[row - 1][col + 1]
    if col - 1 >= 0:
        count += grid[row][col - 1]
    if col + 1 < WIDTH:
        count += grid[row][col + 1]
    if row + 1 < HEIGHT:
        count += grid[row + 1][col]
    if (row + 1 < HEIGHT) and (col - 1 >= 0):
        count += grid[row + 1][col - 1]
    if (row + 1 < HEIGHT) and (col + 1 < WIDTH):
        count += grid[row + 1][col + 1]
    return count

glider_pattern = [[0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0],
                  [0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0]]


glider_gun_pattern = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def load_pattern(pattern, x_offset=0, y_offset=0):
    global GRID_MODEL

    for i in range(0, HEIGHT):
        for j in range(0, WIDTH):
            GRID_MODEL[i][j] = 0

    j = y_offset

    for row in pattern:
        i = x_offset
        for value in row:
            GRID_MODEL[i][j] = value
            i = i + 1
        j = j + 1

if __name__ == "__main__":
    next_gen()
