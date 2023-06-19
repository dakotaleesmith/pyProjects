"""
Kata from codewars: https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
"""


def sort_array(source_array):
    evens = [{"val": val, "index": index} for index, val in enumerate(source_array) if val % 2 == 0]
    array_sorted = sorted([i for i in source_array if i % 2 != 0])
    for even_num in evens:
        array_sorted.insert(even_num["index"], even_num["val"])
    return array_sorted


if __name__ == "__main__":
    test_case = [5, 3, 2, 8, 1, 4]
    result = sort_array(test_case)
    answer = [1, 3, 2, 8, 5, 4]
    print(f"\nResult: {result}\nExpected: {answer}\n")
    assert result == answer, "Sorry, wrong answer!"
