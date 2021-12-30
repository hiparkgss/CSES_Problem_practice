from typing import List


def assign_apartment(people: List[int], apartments: List[int], tolerance: int):
    # assign bigger apartment to people with bigger demand
    people.sort()
    apartments.sort()
    result = 0
    while True:  # loop until lists are empty
        try:
            person = people[-1]  # biggest demand
            apt = apartments[-1]  # biggest apartment supply
        except IndexError:  # empty list
            break

        if person - tolerance <= apt <= person + tolerance:  # demand supply matching
            result += 1
            del apartments[-1]
            del people[-1]
        elif apt > person + tolerance:  # apartment is bigger
            del apartments[-1]
        elif apt < person - tolerance:  # apartment is smaller
            del people[-1]

    return result


# input
raw1 = input().split()
raw2 = input().split()
raw3 = input().split()
N, M, K = list(map(int, raw1))  # k is tolerance
A = list(map(int, raw2))  # people
B = list(map(int, raw3))  # size of apartment
ans = assign_apartment(A, B, K)
print(ans)