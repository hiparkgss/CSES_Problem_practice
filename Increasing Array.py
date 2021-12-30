n = input()
arr_in = list(map(int, input().split()))

# initialisation
previous_max = arr_in.pop(0)
number_of_increment = 0  # this is the ans

for elem in arr_in:
    current_max = max(previous_max, elem)
    number_of_increment += current_max - elem
    # 0 if elem is larger or equal to previous max
    # previous_max - elem is incremented if previous_max is larger.
    previous_max = current_max  # reset the previous_max for the next iteration

print(number_of_increment)
