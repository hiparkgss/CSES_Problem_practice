# https://cses.fi/problemset/task/1662


def comb2(k):
    return max(k * (k - 1) // 2, 0)


n = int(input())
arr = list(map(int, input().split()))
count_remainder = [0] * n
prefix_sum = 0
count_remainder[prefix_sum] += 1
for elem in arr:
    remainder = elem % n
    prefix_sum += remainder
    prefix_sum = prefix_sum % n
    count_remainder[prefix_sum] += 1
ans = sum(comb2(count) for count in count_remainder)
print(ans)
