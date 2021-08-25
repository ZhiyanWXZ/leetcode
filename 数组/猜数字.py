from typing import List


def game(guess: List[int], answer: List[int]) -> int:

    sum = 0
    for i in guess:
        if i in answer:
            sum += 1

    return sum