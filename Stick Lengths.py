# https://cses.fi/problemset/task/1074
from typing import List


def find_median(l: List[int], n) -> int:
    # the problem is to
    # find left or right median.
    # This can be proven mathematically,
    # analysing the specific range
    # where gradient changes from negative to positive.

    result = 0

    # l is sorted list
    median = l[n // 2]
    for elem in l:
        result += abs(elem - median)

    return result


# solution
N = int(input())
p = list(map(int, input().split()))
p.sort()
ans = find_median(p, N)
print(ans)
