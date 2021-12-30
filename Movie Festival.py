def find_movies(_start_end):
    _start_end.sort(key=lambda _t: _t[1])  # sort by the ending time
    result = 0
    ending_time = 0
    for movie_time in _start_end:
        start, end = movie_time
        # starting time of the new movie
        # is after the ending time of the previous movie
        if ending_time <= start:
            result += 1
            ending_time = end  # update ending time
    return result


# solution
n = int(input())
start_end = []
for _ in range(n):
    t = tuple(map(int, input().split()))
    start_end.append(t)
ans = find_movies(start_end)
print(ans)
