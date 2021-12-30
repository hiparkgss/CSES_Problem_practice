from typing import List


def max_num(_arrival: List[int], _leaving: List[int]):
    # sort arrival and leaving
    # add 1 for arrival time, and subtract 1 for leaving time
    _n = len(_leaving)
    result = 0
    count = 0
    _arrival.sort()
    _leaving.sort()
    i = 0
    j = 0
    while i < _n:
        if _arrival[i] < _leaving[j]:  # encounter arrival
            count += 1
            i += 1
            result = max(count, result)  # update the max record of customer
        else:  # encounter leaving
            count -= 1
            j += 1

    return result


# solution
n = int(input())
arrival = []
leaving = []
for _ in range(n):
    a, b = list(map(int, input().split()))
    arrival.append(a)
    leaving.append(b)
ans = max_num(arrival, leaving)
print(ans)
