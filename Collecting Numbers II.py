# https://cses.fi/problemset/task/2217
# too slow. time limit error
import sys
import time


def solve():
    return sum(val_ind[val] > val_ind[val + 1] for val in range(1, n))


def adj_values(v1, v2):
    if v1 == 1:
        v1_small = v1
        v1_large = v1 + 1
    elif v1 == n:
        v1_small = v1 - 1
        v1_large = v1
    else:
        v1_small = v1 - 1
        v1_large = v1 + 1

    if v2 == 1:
        v2_small = v2
        v2_large = v2 + 1
    elif v2 == n:
        v2_small = v2 - 1
        v2_large = v2
    else:
        v2_small = v2 - 1
        v2_large = v2 + 1

    return v1_small, v1_large, v2_small, v2_large


def contribution(v1, v2):
    v1_small, v1_large, v2_small, v2_large = adj_values(v1, v2)

    affected_val = list({v1_small, v1_large, v1, v2_small, v2_large, v2})
    affected_val.sort()
    num = len(affected_val)
    result = 0

    for j in range(num - 1):
        j_ = affected_val[j]
        j_n = affected_val[j + 1]
        if j_ + 1 == j_n:
            s = val_ind[j_]
            l = val_ind[j_n]
            result += s > l  # add 1 if True, add nothing if False

    return result


def edit(i1, i2, v1, v2):

    subtract = contribution(v1, v2)

    # swap the val_ind_dict
    val_ind[v1], val_ind[v2] = i2, i1
    x[i2], x[i1] = v1, v2
    add = contribution(v1, v2)

    return add - subtract


"""
n, m = list(map(int, input().split()))
x = list(map(int, input().split()))

val_ind = {}
for i, v in enumerate(x):
    val_ind[v] = i
ans = solve(val_ind)

for _ in range(m):
    a, b = list(map(int, input().split()))
    e = edit(val_ind, a - 1, b - 1, x[a - 1], x[b - 1])
    ans = ans + e
    sys.stdout.write(str(ans))
    sys.stdout.write("\n")
"""

# """
t1 = time.perf_counter()
store = []
with open("test_input.txt") as f:
    n, m = list(map(int, f.readline().split()))
    x = list(map(int, f.readline().split()))

    val_ind = [0] * (n + 1)
    for i, v in enumerate(x):
        val_ind[v] = i
    ans = solve()

    for _ in range(m):
        a, b = list(map(int, f.readline().split()))
        if a == b:
            e = 0
        else:
            e = edit(a - 1, b - 1, x[a - 1], x[b - 1])
        ans = ans + e
        # sys.stdout.write(str(ans))
        # sys.stdout.write("\n")
t2 = time.perf_counter()
print(t2 - t1)
# """
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
