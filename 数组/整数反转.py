import math


def reverse(x: int) -> int:

    if x == 0:
        return 0
    y = [int(i) for i in str(abs(x))]
    z = 0
    for index, value in enumerate(y):
        z += value * 10 ** index
    print(z)

    if z > 2**31 - 1 or - z < -2**31:
        return 0

    if x < 0:
        return -z
    else:
        return z

if __name__ == "__main__":
    x = 120
    print(reverse(x))

