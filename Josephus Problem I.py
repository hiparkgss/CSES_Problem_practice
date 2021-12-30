import time


def solution(n):
    not_visited = set(range(1, n + 1))
    counter = 0
    index = 1
    while len(not_visited) > 1:

        # counter == 1 means that we skipped 1 element
        # and now remove the current element
        if counter == 1:
            while True:
                remainder = index % n

                # ensure we return n instead of 0.
                if remainder == 0:
                    remainder = n

                if remainder in not_visited:
                    not_visited.remove(remainder)
                    counter = 0
                    yield remainder
                    index += 1
                    break
                else:
                    index += 1
        else:  # counter is zero. need to skip a number which is not visited yet
            remainder = index % n

            # ensure we return n instead of 0.
            if remainder == 0:
                remainder = n

            if remainder in not_visited:
                counter += 1
            index += 1

    remainder = not_visited.pop()
    if remainder == 0:
        remainder = n
    yield remainder


# N = int(input())
N = 2*10**5
t1 = time.perf_counter()
ans = list(solution(N))
# print(*ans)
t2 = time.perf_counter()
print(f"CPU time {t2 - t1}")
