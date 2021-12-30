from typing import Tuple, List

# f(n, a, b) = ways to move {1, ..., n} from position a to b
# is_visited(n, a, b) = move single open element {n} from position a to b
# f(n, 1, 3) is the answer
# recursion: f(n, 1, 3) = f(n - 1, 1, 2) -> is_visited(n, 1, 3) -> f(n - 1, 2, 3)
# recursion: f(n, a, b) = f(n - 1, a, c) -> is_visited(n, a, b) -> f(n - 1, c, b)


def g(n: int, a: int, b: int) -> List[Tuple[int, int]]:
    return [(a, b)]


# utilise memoization
memo = {}


def f(n: int, a: int, b: int) -> List[Tuple[int, int]]:
    try:  # if there is an answer already
        return memo[(n, a, b)]

    except KeyError:

        # base case
        if n == 1:
            answer = g(n, a, b)
            memo[(n, a, b)] = answer
            return answer

        # calculate for nontrivial cases
        tower_position = {1, 2, 3}
        tower_position.discard(a)
        tower_position.discard(b)
        c, = tower_position  # picking the element left behind
        answer = f(n - 1, a, c) + g(n, a, b) + f(n - 1, c, b)
        memo[(n, a, b)] = answer
        return answer


n_in = int(input())
result = f(n_in, 1, 3)
print(len(result))
for t in result:
    print(*t)