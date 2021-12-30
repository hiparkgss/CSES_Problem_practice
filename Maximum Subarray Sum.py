# https://cses.fi/problemset/task/1643
# also in Notion Algorithm notes
from typing import List


def find_crossing_subarr(l: List[int], right_side) -> int:
    """
    :param l:
        input list of int
    :param right_side:
         python index of the right crossing
         l[ : right_side] is the left side = {0, 1, ..., right_side - 1}
         l[right_side : ] is the right side = {right_side, right_side + 1, ..., n - 1}
    :return
        maximum subarray crossing the middle
    """
    # sanity check
    n = len(l)
    if n < 2:  # n is 0 or 1
        raise ValueError(f"list input is too short. len={n}")
    elif right_side < 1:  # 0 or negative
        raise ValueError(f"right_side is too small. right_side={right_side}")

    # base case result. 1 left and 1 right.
    right_result = l[right_side]
    left_result = l[right_side - 1]

    # linear search
    # start with right side
    acc = 0
    for i in range(right_side, n):
        acc += l[i]
        if acc > right_result:
            right_result = acc

    # left side
    acc = 0
    for i in range(right_side - 1, -1, -1):
        acc += l[i]
        if acc > left_result:
            left_result = acc

    return right_result + left_result


def find_max_subarr(l: List[int]) -> int:
    """
    maximum subarray could be solved using divide and conquer paradigm.
    divide into 2 halves, left_half and right_half.
    check the one crossing
    """
    n = len(l)
    if n == 1:
        return l[0]

    # for n = {2, 3, ... }
    # right_side is median if odd n, right median if even n.
    # left_half ~ right_half examples
    # 0 ~ 1
    # 0 ~ 1 2
    # 0 1 ~ 2 3
    # 0 1 ~ 2 3 4
    right_side = n // 2
    left_half = l[:right_side]
    right_half = l[right_side:]
    left_result = find_max_subarr(left_half)
    right_result = find_max_subarr(right_half)
    crossing_result = find_crossing_subarr(l, right_side)
    result = max(left_result, right_result, crossing_result)
    return result


# solution
num = int(input())
lst = list(map(int, input().split()))
ans = find_max_subarr(lst)
print(ans)
