# first try. Wrong. Time limit error


def match_price(prices, customers):
    for customer in customers:
        if len(prices) == 0:  # tickets sold out
            yield -1
        elif prices[0] > customer:  # customer cannot buy the cheapest ticket
            yield -1
        else:
            # use binary search
            low, high = 0, len(prices) - 1
            while low < high:
                mid = (low + high + 1) // 2
                mid_price = prices[mid]
                if customer < mid_price:
                    high = mid - 1
                else:  # customer >= mid_price
                    low = mid

            matching_price = prices.pop(low)  # I think this is slow
            yield matching_price


n, m = list(map(int, input().split()))
h = list(map(int, input().split()))  # ticket price
t = list(map(int, input().split()))  # max price customers can afford
h.sort()
ans = match_price(h, t)
print(*ans, sep='\n')
