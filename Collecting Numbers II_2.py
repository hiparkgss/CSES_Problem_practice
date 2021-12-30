# https://cses.fi/problemset/task/2217
# second try. still time limit error

import sys
import time


def solve():
    return sum(val_ind[val] > val_ind[val + 1] for val in range(1, n))


def edit(i1, i2, answer):
    c = 0

    r, s = x[i1], x[i2]

    if val_ind[r] >= val_ind[r - 1] > i2:
        c += 1
    if val_ind[r] < val_ind[r - 1] <= i2:
        c -= 1
    if val_ind[r] <= val_ind[r + 1] < i2:
        c += 1
    if val_ind[r] > val_ind[r + 1] >= i2:
        c -= 1

    if val_ind[s] >= val_ind[s - 1] > i1:
        c += 1
    if val_ind[s] < val_ind[s - 1] <= i1:
        c -= 1
    if val_ind[s] <= val_ind[s + 1] < i1:
        c += 1
    if val_ind[s] > val_ind[s + 1] >= i1:
        c -= 1

    # swap the val_ind_dict
    val_ind[r], val_ind[s] = i2, i1
    x[i2], x[i1] = r, s

    return c + answer


# """
n, m = list(map(int, input().split()))
x = list(map(int, input().split()))

val_ind = [0] * (n + 2)  # val_ind[0] = 0; minimum
val_ind[n+1] = n + 1  # maximum
for i, v in enumerate(x):
    val_ind[v] = i
ans = solve()

for _ in range(m):
    a, b = list(map(int, input().split()))
    if a == b:
        pass
    else:
        ans = edit(a - 1, b - 1, ans)
    sys.stdout.write(str(ans))
    sys.stdout.write("\n")
# """

"""
t1 = time.perf_counter()
store = []
with open("test_input.txt") as f:
    n, m = list(map(int, f.readline().split()))
    x = list(map(int, f.readline().split()))

    val_ind = [0] * (n + 2)  # val_ind[0] = 0; minimum
    val_ind[n+1] = n + 1  # maximum
    for i, v in enumerate(x):
        val_ind[v] = i
    ans = solve()

    for _ in range(m):
        a, b = list(map(int, f.readline().split()))
        if a == b:
            pass
        else:
            ans = edit(a - 1, b - 1, ans)
        sys.stdout.write(str(ans))
        sys.stdout.write("\n")
t2 = time.perf_counter()
print(t2 - t1)
"""
"""
with open("test_input_result.txt", "w") as f:
    for elem in store:
        f.write(str(elem))
        f.write("\n")

with open("test_input_result.txt", "r") as f:
    a = f.readlines()

with open("test_output.txt", "r") as f:
    b = f.readlines()
"""
