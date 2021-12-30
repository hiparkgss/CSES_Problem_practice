t = int(input())
ab_pairs = []
for i in range(t):
    a, b = map(int, input().split())
    s = a + b
    if s % 3 != 0:
        print("NO")
    else:  # sum up to multiple 3
        large, small = max(a, b), min(a, b)
        if large > 2 * small:
            print("NO")
        else:
            print("YES")

