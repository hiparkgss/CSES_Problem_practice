# https://cses.fi/problemset/task/1073
import bisect


def solution(l):
    end_value = [float('inf')] * N
    low = 0
    for elem in l:
        i = bisect.bisect_left(end_value, elem + 1, low, N)
        end_value[i] = elem
    return sum(elem < float('inf') for elem in end_value)


N = int(input())
K = list(map(int, input().split()))
ans = solution(K)
print(ans)
