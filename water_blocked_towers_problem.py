"""
Problem statement: https://www.geeksforgeeks.org/trapping-rain-water/
"""

def find_water_volume_blocked_in_towers(towers):
    """
    Solution for finding water volume occupied in towers of different heights.
    Assumed that, width of tower is 1 unit.
    :param towers: list of tower heights
    :return: unit water occupied
    """
    res = 0
    n = len(towers)

    for_idx = 0
    # traverse forward
    while (for_idx < n):
        j = for_idx + 1
        sel_towers = []
        while (j < n and towers[for_idx] >= towers[j]):
            sel_towers.append(towers[j])
            j += 1
        if j < n:
            for t_h in sel_towers:
                res += abs(towers[for_idx] - t_h)
        for_idx = j

    back_idx = n - 1
    # traverse backward
    while(back_idx > -1):
        j = back_idx - 1
        sel_towers = []
        while (j > -1 and towers[back_idx] >= towers[j]):
            sel_towers.append(towers[j])
            j -= 1
        if j > -1:
            for t_h in sel_towers:
                res += abs(towers[back_idx] - t_h)
        back_idx = j
    return res

print(find_water_volume_blocked_in_towers([4, 5, 3, 3, 7, 4, 3, 5, 4, 4, 1]))