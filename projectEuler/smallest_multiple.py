"""
Problem #5
Link: https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def main(range_start: int, range_end: int):
    divisors = [n for n in range(range_start, range_end)]
    multiple = divisors[-1] + 1
    validate = any(multiple % num for num in divisors)
    while validate:
        multiple += 1
        validate = any(multiple % num for num in divisors)
    return multiple
    
if __name__ == "__main__":
    print(main(1, 21))