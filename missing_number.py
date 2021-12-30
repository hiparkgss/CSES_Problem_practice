n = int(input())
arr = map(int, input().split())
complete_arr = list(range(0, n + 1))  # use index of complete_arr as the value of the element of arr

for elem in arr:
    complete_arr[elem] = 0  # in the end, the single value left nonzero is the missing one.

print(sum(complete_arr))