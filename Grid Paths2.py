# second try after the first failure
from typing import Tuple
import itertools


def move_position(position: Tuple[int, int], direction: str):
    row, col = position
    if direction == 'D':
        row += 1
        return row, col
    elif direction == 'U':
        row -= 1
        return row, col
    elif direction == 'L':
        col -= 1
        return row, col
    elif direction == 'R':
        col += 1
        return row, col
    else:  # sanity check. should not be reached
        raise ValueError("wrong direction is given other than DULR")


def is_valid_position(position, visited):
    # assume true until an error is found
    # check col and row are within the range
    x, y = position

    if 0 <= x <= grid_size - 1:  # good range
        pass
    else:  # wrong range
        return False

    if 0 <= y <= grid_size - 1:  # good range
        pass
    else:  # wrong range
        return False

    # check the position is not a repetition of is_visited set
    if visited[x][y]:  # visiting the same position twice
        return False

    return True


def is_forward_valid(position, previous_move, visited):
    next_forward_position = move_position(position, previous_move)
    return is_valid_position(next_forward_position, visited)


def is_crash(position, previous_move, visited):
    if is_forward_valid(position, previous_move, visited):
        return False
    # here moving forward direction is not valid
    num_moves = 0
    Directions = "DULR"
    for d in Directions:
        n_p = move_position(position, d)
        if is_valid_position(n_p, visited):
            num_moves += 1
    if num_moves == 2:  # left and right only
        return True

    return False


counter = itertools.count()  # todo delete this before submission


def search_all_paths(position: Tuple[int, int], travel_length,
                     restrictions, visited, previous_move):
    """
    :param previous_move:
    :param position: current position of (row, col)
    :param travel_length: 0 at the initial point.
    :param restrictions: ? for any direction, and DULR for specific moves
    :param visited: nested list of boolean of is_visited or not yet is_visited
    :return:
       0 if the position is invalid.
       subsequent recursion if valid
    """
    next(counter)  # todo delete this before submission

    # firstly, check if the position is at the destination
    if position == final_position:
        if travel_length == maximum_len:  # is_visited all the grids
            return 1
        else:  # reached the destination but not all the other grids
            return 0

    # crashing on the wall or boundaries
    if is_crash(position, previous_move, visited):
        return 0

    # now we are in a valid position.
    row, col = position
    visited[row][col] = True  # marking the current position is true
    Directions = "DULR"
    possible_direction = restrictions[travel_length]
    travel_length += 1

    if possible_direction == '?':
        subproblems = []
        for direction in Directions:
            next_position = move_position(position, direction)
            if not is_valid_position(next_position, visited):
                continue
            # visited_ = copy.deepcopy(is_visited)
            path = search_all_paths(next_position, travel_length, restrictions, visited, direction)
            subproblems.append(path)
        result = sum(subproblems)
        # marking the current position is false after we obtain our answer
        visited[row][col] = False
        return result
    else:  # restrictions
        direction = possible_direction
        next_position = move_position(position, direction)

        if is_valid_position(next_position, visited):
            path = search_all_paths(next_position, travel_length, restrictions, visited, direction)
            # marking the current position is false after we obtain our answer
            visited[row][col] = False
            return path
        else:
            visited[row][col] = False
            return 0


# main solution
grid_size = 7  # we will use python indexing.
# (0, 0) top left corner and  to (6, 6) bottom right.
initial_position = (0, 0)
path_taken_so_far = ''
final_position = (grid_size - 1, 0)
maximum_len = grid_size ** 2 - 1
path_input = '?' * maximum_len  # todo comment this for submission
# path_input = input()  # todo uncomment this for submission
visit_lst = [[False for _ in range(grid_size)] for _ in range(grid_size)]
ans = search_all_paths(initial_position, 0, path_input, visit_lst, 'D')
print(ans)
print("recursion count", next(counter))  # todo delete this before submission
