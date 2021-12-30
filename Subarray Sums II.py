# https://cses.fi/problemset/task/1661
import bisect


def prefix(arr):
    n = len(arr)
    prefix_arr = [0] * (n + 1)  # this is to make 1-indexing
    for i in range(1, n + 1):
        prefix_arr[i] = prefix_arr[i - 1] + arr[i - 1]

    # prefix_arr[i] = arr[0] + ... + arr[i - 1], the first i elements
    # prefix_arr[0] = 0; boundary condition.
    return prefix_arr


def solution(arr, target, n):
    # prefix[b] - prefix[a - 1] = target for some (a <= b)
    # re-arrange into prefix[b] = target + prefix[a - 1]
    # need to carefully choose (a, b) such that a <= b.
    result = 0
    prefix_arr = prefix(arr)
    target_plus = [target + elem for elem in prefix_arr]
    index_map = {}
    plus_target_map = {}
    for i in range(1, n + 1):
        try:
            index_map[prefix_arr[i]].append(i)
        except KeyError:
            index_map[prefix_arr[i]] = [i]

    for a_min_one in range(n):
        try:
            plus_target_map[target_plus[a_min_one]].append(a_min_one)
        except KeyError:
            plus_target_map[target_plus[a_min_one]] = [a_min_one]

    for k, a_min_one_s in plus_target_map.items():
        if k in index_map:
            b_s = index_map[k]
            for b in b_s:
                result += bisect.bisect_left(a_min_one_s, b)

    return result


N, X = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = solution(A, X, N)
print(ans)

"""

A neater solution is given here

from collections import defaultdict


# 5 7
# 2 -1 3 5 -2

def count_subarray_sum(array, n, x):
    sum2index = defaultdict(int)
    count = 0
    sum2index[0] += 1
    prefixsum = 0
    for i in range(n):
        prefixsum += array[i]
        if prefixsum - x in sum2index:
            count += sum2index[prefixsum - x]
        sum2index[prefixsum] += 1

    return count


n, x = list(map(int, input().split(' ')))
array = list(map(int, input().split(' ')))

answer = count_subarray_sum(array, n, x)
print(answer)

"""
