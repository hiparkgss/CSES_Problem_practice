import itertools as it

n = int(input())
weights = list(map(int, input().split()))
weights_sum = sum(weights)

# since n is small, 2**n is approximately 10**6, we can use brute force
# w1: List contains all the weights.
# our aim is to relocate m number of weights to w2: List, and minimise the difference.
# m ranges from 1 to n//2

result = weights_sum  # maximum value it can get
for m in range(1, n // 2 + 1):  # for m number of w2
    # pick the index that we would like to relocate to w2
    for indices_of_w2 in it.combinations(range(n), r=m):
        w2 = [weights[index] for index in indices_of_w2]
        w2_sum = sum(w2)
        difference = abs(weights_sum - 2 * w2_sum)
        if difference < result:
            result = difference

print(result)
