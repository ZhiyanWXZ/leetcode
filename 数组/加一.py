from typing import List


def plusOne(digits: List[int]) -> List[int]:

    if digits[-1] + 1 < 10:
        digits[-1] += 1
        return digits
    digits[-1] = 0
    carry = 1
    index = -2
    while carry == 1 and index >= -len(digits):
        if digits[index] + carry < 10:
            digits[index] += 1
            return digits
        digits[index] = 0
        index -= 1
    digits.insert(0, 1)
    return digits


if __name__ == "__main__":
    digits = [9,9,9,9,9,9]
    plusOne(digits)
    print(digits)




