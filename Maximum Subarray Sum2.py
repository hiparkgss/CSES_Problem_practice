# https://cses.fi/problemset/task/1643
# also in Notion Algorithm notes
from typing import List


def find_max_subarray(A: List[int]) -> int:
    g = A[0]
    min_g = 0
    h = g - min_g
    for elem in A[1:]:
        min_g = min(min_g, g)
        g += elem
        h = max(h, g - min_g)
    return h


# solution
num = int(input())
lst = list(map(int, input().split()))
ans = find_max_subarray(lst)
print(ans)
