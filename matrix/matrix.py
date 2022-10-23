from random import randint
from time import sleep

def reroll(list_nums):
    """Takes list of numbers and "rerolls" (and prints) them until all numbers match."""
    key = int(list_nums[0])
    match_index = 1

    while match_index < len(list_nums):
        if int(list_nums[match_index]) != key:
            for i, n in enumerate(list_nums[match_index:], start=match_index):
                list_nums[i] = randint(0, 9)
            sleep(0.05)
            print(list_nums)
        else:
            match_index += 1

RANGE_END = 30
initial_roll = [randint(0, 9) for n in range(0, RANGE_END)]

if __name__ == "__main__":
    print(initial_roll)
    reroll(initial_roll)
