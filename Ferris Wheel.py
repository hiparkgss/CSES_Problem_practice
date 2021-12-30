from collections import deque
from typing import List
from collections import deque


# bin-packing problem.
# start with the heaviest child and try the lightest to fit that boat
def find_num_gondola(capacity: int, children: List[int]):
    half_capacity = capacity / 2
    light = []
    heavy = deque()
    # cannot have 2 heavy kids in 1 boat.
    # In a boat, there could be 2 people only if one heavy and one light or 2 lights
    for child in children:
        if child <= half_capacity:
            light.append(child)
        else:
            heavy.append(child)

    boat = 0
    while light:  # until all the light children are assigned
        heaviest_in_light = light.pop()

        # it cannot fit in the boat of the lightest child in heavy group
        if len(heavy) == 0:
            heavy.append(heaviest_in_light)
        # elif len(heavy) == 1:
        #     if heaviest_in_light + heavy[0] <= capacity:
        #         boat += 1
        #         del heavy[0]
        #     else:
        #         heavy.appendleft(heaviest_in_light)

        # there are 1 or more children in heavy group
        elif heaviest_in_light + heavy[0] > capacity:
            heavy.appendleft(heaviest_in_light)
        else:  # can share a boat
            i = 0
            while heaviest_in_light + heavy[i] <= capacity:
                if i == len(heavy) - 1:  # reached the end
                    i += 1
                    break
                i += 1
            del heavy[i - 1]
            boat += 1  # one boat is assigned to accommodate 2 people

    boat += len(heavy)  # add remaining heavy groups
    return boat


# solution
n, x = list(map(int, input().split()))
p = list(map(int, input().split()))
p.sort()
ans = find_num_gondola(x, p)
print(ans)
