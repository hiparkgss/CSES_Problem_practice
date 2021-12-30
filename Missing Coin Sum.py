# https://cses.fi/problemset/task/2183
from typing import List
import collections as col

# analyse this algorithm


def find_missing(l: List[int]) -> int:
    """
    Algorithm explained:
    Let's say we have distinct int list in ascending order: D
    The count of each element of D is given as C.

    Assume that {1, 2, ..., D[i] - 1} can be expressed as a sum of {D[0], ..., D[i-1]}.
    Then, sum D[k] * C[k] for k = 1, ..., i are expressible by {D[0], ..., D[i]}.

    Proof by recursion.
    By construct, we can express from 1 to D[i] * C[i] + (D[i] - 1),
    using the sum of {D[0], ..., D[i]} with {C[0], ..., C[i]} respectively.
    Note that it is possible to express from 1 to D[i-1] - 1 using the sum of {D[0], ..., D[i-2]}.
    Therefore, we can express from 1 to D[i] * C[i] + D[i-1] *C[i-1] + (D[i-1] -1)

    It is sufficient to impose a condition
    that accumulation (i.e. sum of A[0], ..., A[j]) >= D[j] - 1
    for all j.

    :param l:
        sorted integer array
    :return:
        the smallest missing sum
    """
    # trivial case
    if l[0] != 1:
        return 1

    c = col.Counter(l)
    distinct = list(c)
    accumulation = 0

    for elem in distinct:
        if accumulation >= elem - 1:  # fine
            accumulation += elem * c[elem]
        else:  # wrong
            return accumulation + 1

    return accumulation + 1


# solution
N = int(input())
X = list(map(int, input().split()))
X.sort()
ans = find_missing(X)
print(ans)
