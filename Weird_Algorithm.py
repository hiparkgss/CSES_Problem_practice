a = int(input())


def operator(i):
    result = [i]

    if i == 1:
        return result

    while i != 1:
        if i % 2 == 1:  # odd
            i = 3 * i + 1
            result.append(i)
        elif i % 2 == 0:  # even
            i = i // 2
            result.append(i)

    return result


l = operator(a)
print(*l)
