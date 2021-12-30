from typing import List


def calculate_distinct_numbers(l: List[int]):
    l = sorted(l)
    last_elem = l.pop()
    result = 1
    d = len(l)
    for i in range(-1, -d - 1, -1):
        if l[i] == last_elem:
            pass
        else:
            result += 1
            last_elem = l[i]

    return result


# main
n = int(input())
raw_input_lst = list(map(int, input().split()))
ans = calculate_distinct_numbers(raw_input_lst)
print(ans)