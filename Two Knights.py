def two_knights_problem(k):
    """
    find the two knights problem for large k, at least bigger than 8
    :param k:
    :return:
    """
    answer = [0, 6, 28, 96, 252, 550, 1056, 1848]
    n_ans = len(answer)

    if k <= n_ans:  # large
        return answer[k - 1]

    size = k ** 2

    # for the inner (k-4) by (k-4) areas, there are 9 unavailable spots
    num_unavail_spots = [9]
    multiplicity = [(k - 4) ** 2]

    # 7 unavailable spots in depth 2
    num_unavail_spots.append(7)
    multiplicity.append(4 * (k - 4))

    # 5 unavailable spots in depth 1
    num_unavail_spots.append(5)
    multiplicity.append(4 * (k - 4))

    # 4 corners of 2 by 2
    num_unavail_spots.append(5)
    multiplicity.append(4)

    num_unavail_spots.append(4)
    multiplicity.append(8)

    num_unavail_spots.append(3)
    multiplicity.append(4)

    # calculate
    result = 0

    def f(unavail, mul, k_sq):
        return mul * (k_sq - unavail) // 2

    for i in range(len(num_unavail_spots)):
        result += f(num_unavail_spots[i], multiplicity[i], size)
    return result


n = int(input())

for j in range(1, n+1):
    print(two_knights_problem(j))
