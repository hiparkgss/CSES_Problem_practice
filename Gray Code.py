n = int(input())

# construct Grey code
result = ['0', '1']
for i in range(1, n):
    temp = []  # temporarily store the result at n = i+1
    for s in result:
        temp.append('0' + s)
    for s in result[::-1]:
        temp.append('1' + s)
    result = temp

print(*result, sep='\n')
