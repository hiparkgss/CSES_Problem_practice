n = int(input())
remainder = n % 4

if remainder == 1 or remainder == 2:
    print("NO")
elif remainder == 3:
    l = list(range(1, n + 1))
    odd = []
    even = [n]
    m = (n - 3)//4
    for i in range(1, 2 * m + 2):
        if i % 2 == 1:  # odd
            odd.append(i)
            odd.append(n - i)
        else:  # even
            even.append(i)
            even.append(n - i)

    print("YES")
    print(len(odd))
    print(*odd)
    print(len(even))
    print(*even)
else:  # multiple of 4
    m = n//4
    outer = []
    inner = []
    for i in range(m):
        outer.append(4 * i + 1)
        outer.append(4 * i + 4)
        inner.append(4 * i + 2)
        inner.append(4 * i + 3)
    print("YES")
    print(len(outer))
    print(*outer)
    print(len(inner))
    print(*inner)
