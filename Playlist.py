# https://cses.fi/problemset/task/1141


def solution(k):
    result = 0
    length = 0
    playlist = set()
    low = 0
    for high in range(N):
        if k[high] in playlist:
            while k[low] != k[high]:
                playlist.remove(k[low])
                length -= 1
                low += 1
            low += 1
        else:
            length += 1
            playlist.add(k[high])
            result = max(length, result)

    return result


N = int(input())
K = list(map(int, input().split()))
ans = solution(K)
print(ans)
