# problem... it takes too long. more efficient algorithm is needed.

# use directed single-edge graph to visualise the overall problem.
# graph node is the path (of various length) taken from the starting point.
# At a given node, the outgoing edges are possible moves from that situations (i.e. node)
# find the paths that have length 48, and ended up in the correct destination
# use queue data structure to iterate while loop, until we finish at length 48.

# initialisation
from typing import Tuple
from collections import deque

# path_input = input()
path_input = "????????????????????????????????????????????????"
grid_size = 7  # we will use python indexing.
# (0, 0) top left corner and  to (6, 6) bottom right.
initial_position = (0, 0)
path_taken_so_far = ''
final_position = (grid_size - 1, 0)
max_grid_size = grid_size ** 2 - 1


def move(direction: str, position: Tuple[int, int]):
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


def is_valid_position(position, visited_set):
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
    if position in visited_set:  # visiting the same position twice
        return False

    return True


def find_paths(current_position: Tuple[int, int], path_str: str, visited_positions: set):
    """

    :param current_position: (row, column)
    :param path_str: path taken so far represented in string.
    :param visited_positions: set of past positions (row, column)
    :return: list of (next_position, updated path_str, updated visited_positions, current_available_paths)
    """
    result = []
    possible_directions = 'DULR'
    current_available_paths: int = 0  # available number of pathways at the current_position
    for direction in possible_directions:
        next_position = move(direction, current_position)
        if is_valid_position(next_position, visited_positions):  # valid move
            visited_positions_set = visited_positions.copy()
            visited_positions_set.add(current_position)
            t = [next_position, path_str + direction, visited_positions_set, 0]
            result.append(t)
            current_available_paths += 1

    # add information about number of available paths
    for elem in result:
        elem[-1] += current_available_paths

    return result


# main function
# initialisation of main function
possible_paths = []
visited_nodes = set()
q = deque()
initial = (0, 0), '', set(), 2
q.append(initial)

loop_counter = 0
# while loop for main function
while q:  # loop continues while q is non-empty

    # todo delete this part
    loop_counter += 1
    if loop_counter == 10 ** 8:
        print("loop counter limit")
        break

    curr_position, path_in_str, prev_visited_set, num_prev_paths = q.pop()
    if path_in_str not in visited_nodes:  # DFS check
        visited_nodes.add(path_in_str)  # mark as is_visited
        if curr_position == final_position:  # finish the journey at the destination
            if len(path_in_str) == max_grid_size:  # is_visited all the squares. end of journey
                possible_paths.append(path_in_str)
            else:  # wrong ending
                continue
        elif len(path_in_str) < max_grid_size:  # far more way to go
            next_moves = find_paths(curr_position, path_in_str, prev_visited_set)
            for next_move in next_moves:  # check each move
                num_curr_paths = next_move[-1]
                if num_prev_paths == 3 and num_curr_paths == 2:  # block in the middle
                    continue
                else:
                    q.append(next_move)

"""
# count the matching paths
def count_paths(poss_paths, requirement):
    # req_dict = {direction, list of indices}
    req_dict = dict(D=[], U=[], L=[], R=[])
    for i in range(len(requirement)):
        if requirement[i] == '?':  # free
            continue
        else:  # requirement
            req_dict[requirement[i]].append(i)

    count = 0
    for path in poss_paths:
        is_valid = True
        for k, v in req_dict.items():
            if any(path[ind] != k for ind in v):  # at least one requirement violated
                is_valid = False
            else:  # all requirements are satisfied
                pass
        count += is_valid

    return count
"""

# ans = count_paths(possible_paths, path_input)
ans = len(possible_paths)
print(ans)
