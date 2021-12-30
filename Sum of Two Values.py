from typing import List


def sol(arr: List[int], s: int):
    if n == 1:
        return "IMPOSSIBLE",
    index_map = {}  # value: [index]
    for i in range(n):
        try:
            index_map[arr[i]].append(i)
        except KeyError:
            index_map[arr[i]] = [i]

    arr.sort()
    i = 0
    j = n - 1
    r = s - arr[j]
    while i < j - 1:
        if r > arr[i]:
            i += 1
        elif r == arr[i]:
            break
        else:  # r < arr[i] case
            j -= 1
            r = s - arr[j]

    if arr[i] + arr[j] == s:
        l1 = index_map[arr[i]]
        l2 = index_map[arr[j]]
        return l1.pop() + 1, l2.pop() + 1
    else:
        return "IMPOSSIBLE",


# solution
n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = sol(a, x)
print(*ans)
