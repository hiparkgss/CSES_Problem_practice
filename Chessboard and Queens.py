import copy
from collections import deque
from typing import List


n = 8
chess_input = []
for i in range(n):
    line = input()
    b = [elem == '.' for elem in line]  # True means position is free
    chess_input.append(b)

# n = 8
# chess_input = []
# for i in range(n):
#     chess_input.append([True] * 8)


def remove(grid: List[List[int]], row: int, col: int):
    num_row = len(grid)
    num_col = len(grid[0])

    # sanity check
    if num_row != num_col:
        raise ValueError("not a square grid")
    if row >= num_row:
        raise ValueError("row position is bigger than the grid")
    if col >= num_col:
        raise ValueError("col position is bigger than the grid")

    # 1 main diagonal
    increment = min(num_row - row, num_col - col)
    decrement = min(row + 1, col + 1)
    for inc in range(increment):
        grid[row + inc][col + inc] = False
    for dec in range(decrement):
        grid[row - dec][col - dec] = False

    # 2 anti diagonal
    increment = min(row + 1, num_col - col)
    decrement = min(num_row - row, col + 1)
    for inc in range(increment):
        grid[row - inc][col + inc] = False
    for dec in range(decrement):
        grid[row + dec][col - dec] = False

    # 3 remove col
    for r in grid:
        r[col] = False

    # 4 remove row
    grid[row] = [False] * num_col

    return grid


def locate_queen(grid, row, col):
    # if this function returns True, [[]] empty list, then we should count 1.
    return grid[row][col], remove(grid, row, col)


def count_queen_location(init_grid):
    q = deque()  # queue

    # initialisation
    count = 0
    size = len(init_grid)
    row = 0  # start from the top row
    for col in range(size):
        initial_grid = copy.deepcopy(init_grid)
        q.append((row, col, initial_grid))

    while q:  # continues if q_in is non-empty
        row, col, grid = q.popleft()
        is_possible, modified_grid = locate_queen(grid, row, col)
        if is_possible:  # this means that grid[row][col] was free
            row += 1  # row = size - 1 means the last row.
            if row == size:  # end of process
                count += 1
            else:  # we need to continue to shrink the grid
                for col in range(size):
                    next_grid = copy.deepcopy(modified_grid)
                    q.append((row, col, next_grid))

    return count


ans = count_queen_location(chess_input)
print(ans)
