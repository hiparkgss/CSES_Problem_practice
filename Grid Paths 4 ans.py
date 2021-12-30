# this is the solution but cannot pass time limit with python.

is_visited = [[False for i in range(7)] for j in range(7)]  # is_visited


def f(y, x, i, m):
    """

    :param y: row index. python 0 indexing
    :param x: column index. python 0 indexing
    :param i: travel length. s[i] is the direction of the current iteration
    :param m: previous direction.
    :return:
    """
    if i == 48:
        return 1
    if is_visited[6][0]:
        return 0

    # wall or boundary crashing.
    if (m == 'L' and (x == 0 or is_visited[y][x - 1])
            and 0 < y < 6 and not is_visited[y - 1][x] and not is_visited[y + 1][x]):
        return 0
    if (m == 'R' and (x == 6 or is_visited[y][x + 1])
            and 0 < y < 6 and not is_visited[y - 1][x] and not is_visited[y + 1][x]):
        return 0
    if (m == 'U' and (y == 0 or is_visited[y - 1][x])
            and 0 < x < 6 and not is_visited[y][x - 1] and not is_visited[y][x + 1]):
        return 0
    if (m == 'D' and (y == 6 or is_visited[y + 1][x])
            and 0 < x < 6 and not is_visited[y][x - 1] and not is_visited[y][x + 1]):
        return 0

    # direction of the current position
    if s[i] == '?':
        r = [-1, 0, 1, 0]
        c = [0, -1, 0, 1]
        k = 0
        for j in range(4):
            yy = y + r[j]
            xx = x + c[j]
            # check if the next point is valid
            if yy < 0 or yy > 6:
                continue
            if xx < 0 or xx > 6:
                continue
            if is_visited[yy][xx]:
                continue
            is_visited[yy][xx] = True
            k += f(yy, xx, i + 1, 'ULDR'[j])
            is_visited[yy][xx] = False
        return k

    if s[i] == "L":
        x -= 1
    elif s[i] == 'R':
        x += 1
    elif s[i] == 'U':
        y -= 1
    elif s[i] == 'D':
        y += 1
    if x < 0 or x > 6:
        return 0
    if y < 0 or y > 6:
        return 0
    if is_visited[y][x]:
        return 0
    is_visited[y][x] = True
    k = f(y, x, i + 1, s[i])
    is_visited[y][x] = False  # back-tracking after calculating k
    return k


# s = input()
s = '????????????????????????????????????????????????'
is_visited[0][0] = True
print(f(0, 0, 0, 0))
