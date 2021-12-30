t = int(input())
y_x_pairs = []  # [(y1, x1), (y2, x2), ... ]
max_size = []  # maximum coordinate between col and row
while t:
    t -= 1
    pair = input()
    if pair:
        pair = tuple(map(int, pair.split()))
        y_x_pairs.append(pair)
        max_size.append(max(pair))
    else:
        break

# make a dict of diagonal element
# [0: 1, 1: 3, 2: 7, 3: 13, 4: 21, ...] until it includes all the y_x_pairs
diagonal = {}
# n = max(max_size)
n = 10 ** 9


def calculate_diagonal_element(n):
    """
    n th (python indexing) diagonal
    :param n:
    :return:
    """
    return 1 + n ** 2 + n


# now print the element
for y, x in y_x_pairs:
    # adjust to python indexing
    y -= 1
    x -= 1

    # upper triangular
    if y < x:  # (0, 4)
        d = x  # dth diagonal is applicable
        if d % 2 == 0:  # ascending in up
            try:
                e = diagonal[d]  # (d, d) in the 2d matrix
            except KeyError:
                diagonal[d] = calculate_diagonal_element(d)
                e = diagonal[d]
            print(e + d - y)
        else:  # ascending in down
            try:
                e = diagonal[d]  # (d, d) in the 2d matrix
            except KeyError:
                diagonal[d] = calculate_diagonal_element(d)
                e = diagonal[d]
            print(e - d + y)

    #  lower triangular
    else:  # (3, 3) or (4, 1)
        d = y
        if d % 2 == 0:  # ascending in right
            try:
                e = diagonal[d]  # (d, d) in the 2d matrix
            except KeyError:
                diagonal[d] = calculate_diagonal_element(d)
                e = diagonal[d]
            print(e - d + x)
        else:  # ascending in left
            try:
                e = diagonal[d]  # (d, d) in the 2d matrix
            except KeyError:
                diagonal[d] = calculate_diagonal_element(d)
                e = diagonal[d]
            print(e + d - x)
