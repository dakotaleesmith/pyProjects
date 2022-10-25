"""
Problem #1
Link: https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def check_if_multiple(multiple: int, num: int) -> bool:
    if num % multiple == 0:
        return True
    else:
        return False

def main():
    multiples = [num for num in range(0, 1000) if check_if_multiple(3, num) | check_if_multiple(5, num)]
    answer = sum(multiples)
    return answer

if __name__ == "__main__":
    print(main())