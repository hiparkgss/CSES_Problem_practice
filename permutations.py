n = int(input())
arr = list(range(1, n+1))

if n == 1:
    print(*arr)
elif n == 2 or n == 3:
    print("NO SOLUTION")
else:  # construct a required permutation
    odd = arr[::2]
    even = arr[1::2]
    result = even + odd  # [2, 4, 1, 3] for example
    print(*result)


