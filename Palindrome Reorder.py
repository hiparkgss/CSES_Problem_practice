s = input()
n = len(s)
d = {}

# make a frequency dictionary
for char in s:
    try:
        d[char] += 1
    except KeyError:
        d[char] = 1

# check which characters are used odd times
odd_char = []
for k, v in d.items():
    if v % 2 == 1:  # char is used odd times
        odd_char.append(k)

num_of_odds = len(odd_char)
if num_of_odds > 1:
    print("NO SOLUTION")

elif num_of_odds == 1:
    result = []
    for k, v in d.items():
        if k == odd_char[0]:  # we need to skip this
            mid = len(result)//2
            result = result[:mid] + [k] * v + result[mid:]
        else:
            half_times = v//2
            result = [k] * half_times + result + [k] * half_times
    answer = "".join(result)
    print(answer)

else:  # no character is used odd times
    result = []
    for k, v in d.items():
        half_times = v//2
        result = [k] * half_times + result + [k] * half_times
    answer = "".join(result)
    print(answer)