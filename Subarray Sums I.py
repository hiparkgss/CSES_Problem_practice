# https://cses.fi/problemset/task/1660


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
    # basically, target_plus[a - 1] is equal to prefix[b] for some (a, b) uniquely
    # because prefix has distinct elements and is sorted,
    # which is due to the fact that the original arr has positive elements only.
    prefix_arr = prefix(arr)
    target_plus = [target + elem for elem in prefix_arr]
    a = set(prefix_arr)
    b = set(target_plus)
    c = a.intersection(b)
    return len(c)


N, X = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = solution(A, X, N)
print(ans)
