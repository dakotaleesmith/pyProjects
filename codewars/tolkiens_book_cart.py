"""
Kata from codewars: https://www.codewars.com/kata/59a2666349ae65ea69000051/train/python

Tolkein's publisher wishes to implement an online store for the "Lord of the Rings" and "The Hobbit" books. Each book costs $10. However, if 2 titles are purchased, a 5% discount will be received, i.e. purchasing "Fellowship of the Ring" and "Two Towers" will cost $19. If 3 different titles are purchased, a 10% discount will be received. The purchase of all 4 different titles will receive a 20% discount. An additional single title will be full-price.

The encoding of an order will be in the form of strings in an array. For example: [“F”, “T”, “R”, “H”, “H”] is the encoding of 2 copies of "The Hobbit" and a single copy of each of the titles in the "Lord of the Rings" trilogy.

The expected output is a number. E.g. 42 is the expected output for the example above. The output should be the cheapest total cost. For example - if the book order is ["F", "T", "H", "F", "T", "R"], valid total costs include (3*10 discounted by 10%) + (3*10 discounted by 10%) and (4*10 discounted by 20%) + (2*10 discounted by 5%). The cheapest total cost is 51.

This is a slightly simplified version of http://codingdojo.org/kata/Potter/
"""

from collections import Counter

BOOK_PRICE = 10
discounts = {
    2: (2 * BOOK_PRICE) - 2 * BOOK_PRICE * 0.05,
    3: (3 * BOOK_PRICE) - 3 * BOOK_PRICE * 0.1,
    4: (4 * BOOK_PRICE) - 4 * BOOK_PRICE * 0.2,
}


def calculate_cart_total(contents):
    cart_total = 0
    title_totals = Counter(contents)
    while len([i for i in title_totals if title_totals[i] > 0]) > 1:
        num_unique_titles = len([i for i in title_totals if title_totals[i] > 0])
        cart_total += discounts[num_unique_titles]
        for title in title_totals:
            if title_totals[title] > 0:
                title_totals[title] -= 1
    cart_total += BOOK_PRICE * sum(title_totals.values())
    return cart_total


if __name__ == "__main__":
    test_contents = ["F", "T", "R", "H", "R", "R", "T"]
    cart_total = calculate_cart_total(test_contents)
    print(cart_total)
