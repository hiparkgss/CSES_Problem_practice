from collections import deque


def solution(n):
    # initially n people
    pass


if __name__ == '__main__':
    N = 2 * 10 ** 5
    ans = solution(N)
    print(*ans)


##########
n = int(input())
a, b = 1, 0
while(n>0):
    for i in range(2, n + 1, 2):
        print(a * i + b, end=' ')
    if (n&1):
        print(a + b, end=' ')
        b += a
    else:
        b -= a
    a <<= 1
    n >>= 1
