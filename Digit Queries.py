q_in = int(input())
k_in = list(map(int, [input() for dummy in range(q_in)]))

# memo
num_in_k_digit = {digit: digit*(10 ** digit - 10 ** (digit - 1)) for digit in range(1, 18)}


def index_k(k):
    for dummy in range(1, 18):
        num_in_digit = num_in_k_digit[dummy]
        if num_in_digit < k:  # increment num_in_digit
            k = k - num_in_digit
        else:  # k is between 10**(dummy-1) and 10**dummy - 1
            q, r = divmod(k, dummy)
            if r == 0:
                s = str(10**(dummy-1) + q - 1)
                return s[-1]
            else:  # there is a nonzero remainder r
                s = str(10**(dummy-1) + q)
                return s[r-1]


for kth in k_in:
    print(index_k(kth))