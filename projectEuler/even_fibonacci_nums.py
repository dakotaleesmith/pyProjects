"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

Link: https://projecteuler.net/problem=2
"""

def get_fibonacci_sequence(term_limit: int) -> list:
    sequence = [n for n in range(1, 4)]
    last_term = sequence[-1]
    while last_term < term_limit:
        last_two_terms = sequence[-2:]
        next_term = sum(last_two_terms)
        if next_term < term_limit:
            sequence.append(next_term)
            last_term = sequence[-1]
        else:    
            return sequence

def main():
    sequence = get_fibonacci_sequence(4_000_000)
    even_fibonacci_numbers = [num for num in sequence if num % 2 == 0]
    print(sum(even_fibonacci_numbers))

if __name__ == "__main__":
    main()