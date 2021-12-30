n = int(input())

# find the number of 5
multiplicity_of_five = n//5
result = 0
while multiplicity_of_five:
    result += multiplicity_of_five
    multiplicity_of_five = multiplicity_of_five//5

print(result)
