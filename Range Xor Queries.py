# https://cses.fi/problemset/task/1650/
import sys


def xor_prefix(arr, n):
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] ^ arr[i - 1]
    return prefix


def xor_sum_range(prefix, a, b):
    return prefix[b] ^ prefix[a - 1]


N, Q = map(int, sys.stdin.readline().split())
X = list(map(int, sys.stdin.readline().split()))
xor_sum_prefix = xor_prefix(X, N)
for _ in range(Q):
    A, B = map(int, sys.stdin.readline().split())
    ans = xor_sum_range(xor_sum_prefix, A, B)
    sys.stdout.write(str(ans))
    sys.stdout.write("\n")
