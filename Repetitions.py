dna = input()

"""
# this one failed due to time limit. O(n logn)

def find_repetition(s):
    # a repetition of maximum length is located in one of the following:
    left half, right half, or across centre. 
    
    ns = len(s)

    # base case
    if ns == 1:
        return ns

    half = ns // 2
    left, right = s[:half], s[half:]
    centre = 0
    if left[-1] == right[0]:  # then there is a repetition of size at least 2, across the left and right
        centre += 2

        # moving toward left to s[half]
        for seq in left[-2::-1]:
            if seq == s[half]:
                centre += 1
            else:
                break

        # moving toward right to s[half]
        for seq in right[1:]:
            if seq == s[half]:
                centre += 1
            else:
                break

    # divide and conquer
    return max(centre, find_repetition(left), find_repetition(right))
"""

"""
def find_repetition(s):
    # list with values of repetition
    # initialisation
    result = [1]
    previous_seq = s[0]

    # starting with the second DNA seq
    for seq in s[1:]:
        if seq == previous_seq:  # current seq matches the previous
            repetition_length = result[-1] + 1
            result.append(repetition_length)

        else:  # current seq does not match the previous
            result.append(1)  # start repetition length again from 1

        previous_seq = seq  # reset the previous_seq to the current seq for the next iteration

    return max(result)
"""


def find_repetition(s):  # second try
    # list with values of repetition
    # initialisation
    result = 1
    current_count = 1
    previous_seq = s[0]

    # starting with the second DNA seq
    for seq in s[1:]:
        if seq == previous_seq:  # current seq matches the previous
            current_count = current_count + 1
            result = max(current_count, result)

        else:  # current seq does not match the previous
            current_count = 1  # start repetition length again from 1

        previous_seq = seq  # reset the previous_seq to the current seq for the next iteration

    return result


print(find_repetition(dna))
