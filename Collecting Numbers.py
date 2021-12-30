# https://cses.fi/problemset/task/2216

n = int(input())
arr = list(map(int, input().split()))
ans = 0
val_ind = {}
visited = set()
for ind, val in enumerate(arr):
    val_ind[val] = ind

for elem in arr:

    if elem in visited:
        continue

    i = val_ind[elem]
    ans += 1

    for v in range(elem + 1, n + 1):
        j = val_ind[v]
        if j > i:
            i = j
            visited.add(v)
        else:
            break


print(ans)
