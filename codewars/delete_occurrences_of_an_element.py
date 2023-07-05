"""
Kata from codewars: https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python

Enough is enough!
Alice and Bob were on a holiday. Both of them took many pictures of the places they've been, and now they want to show Charlie their entire collection. However, Charlie doesn't like these sessions, since the motif usually repeats. He isn't fond of seeing the Eiffel tower 40 times.
He tells them that he will only sit for the session if they show the same motif at most N times. Luckily, Alice and Bob are able to encode the motif as a number. Can you help them to remove numbers such that their list contains each number only up to N times, without changing the array?

Task
Given a list and a number, create a new list that contains each number of list at most N times, without reordering.
For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
With list [20,37,20,21] and number 1, the result would be [20,37,21].
"""

from collections import Counter


def get_elements_over_limit(array, limit):
    tally = Counter(array)
    return [i[0] for i in tally.items() if i[-1] > limit]


def delete_nth(array, limit):
    elements_over_limit = get_elements_over_limit(array, limit)
    indexed_array_reversed = reversed(list(enumerate(array)))
    for idx, element in indexed_array_reversed:
        if element in elements_over_limit:
            del array[idx]
            elements_over_limit = get_elements_over_limit(array, limit)
    return array


if __name__ == "__main__":
    test_list = [1, 1, 3, 3, 7, 2, 2, 2, 2]
    result = delete_nth(test_list, 3)
    print(result)
