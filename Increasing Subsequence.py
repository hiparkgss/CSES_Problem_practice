# https://cses.fi/problemset/task/1145
from bisect import bisect_left

inf = float('inf')


# longest_increasing_subsequence
def lis(arr):
    # define dp
    dp = [-inf] + [inf] * N

    # scan through arr[i]
    for i in range(N):
        j = bisect_left(dp, arr[i])  # dp[j-1] < arr[i] <= dp[j]
        dp[j] = arr[i]

    return sum(elem < inf for elem in dp) - 1


N = int(input())
X = list(map(int, input().split()))
ans = lis(X)
print(ans)
