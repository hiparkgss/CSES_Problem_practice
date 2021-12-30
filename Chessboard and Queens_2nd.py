import itertools as it

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

possible_positions = []
for per in it.permutations(range(n)):
    possible_positions.append(list(enumerate(per)))

allowed_positions = []  # allowed by constraints given by reserved spaces

for positions in possible_positions:
    are_positions_allowed = True
    for queen_row, queen_col in positions:
        if chess_input[queen_row][queen_col]:  # True if the position is free
            continue
        else:
            are_positions_allowed = False
            break

    if are_positions_allowed:
        allowed_positions.append(positions)


def is_valid(positions_of_queens):  # check if queens can attack diagonally
    choice_of_two = it.combinations(positions_of_queens, 2)
    for queen1, queen2 in choice_of_two:
        x1, y1 = queen1
        x2, y2 = queen2
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        if dx == dy:
            return False
        else:
            pass

    return True


ans = sum(is_valid(positions) for positions in allowed_positions)

print(ans)
