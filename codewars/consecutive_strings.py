"""
Kata from codewars: https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python
"""


def longest_consec(array, n):
    array_length = len(array)
    
    # Exit conditions
    array_empty = array_length == 0
    n_not_valid = n <= 0
    n_longer_than_array_length = n > array_length

    # Default value for "longest"
    longest = ""

    # Assess for conditions
    if any([array_empty, n_not_valid, n_longer_than_array_length]):
        pass

    # Determine longest concatenation
    else:
        for index in range(len(array)):
            concat = "".join(array[index : index + n])
            if len(concat) > len(longest):
                longest = concat

    return longest


if __name__ == "__main__":
    test_array = ["zone", "abigail", "theta", "form", "libe", "zas"]
    result = longest_consec(test_array, 2)
    print(result)
