"""
Kata from codewars: https://www.codewars.com/kata/5442e4fc7fc447653a0000d5/train/python

The goal of this Kata is to return the greatest distance of index positions between matching number values in an array or 0 if there are no matching values.

Example: In an array with the values [0, 2, 1, 2, 4, 1] the greatest index distance is between the matching '1' values at index 2 and 5. Executing greatestDistance/greatest_distance/GreatestDistance with this array would return 3. (i.e. 5 - 2)
"""

def greatest_distance(array):
    indexes = [{"val": val, "index": index} for index, val in enumerate(array)]
    vals = tuple({i for i in array})
    distances = []
    for val in vals:
        sorted_indexes = sorted([i["index"] for i in indexes if i["val"] == val])
        distances.append(sorted_indexes[-1] - sorted_indexes[0])
    return max(distances)


if __name__ == "__main__":
    test_array = [9, 7, 1, 2, 3, 7, 0, -1, -2]
    answer = 4
    result = greatest_distance(test_array)
    print(f"Result: {result}\nExpected: {answer}")
    assert result == answer, "Sorry, wrong answer!"
