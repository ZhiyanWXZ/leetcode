

def mySqrt(x: int) -> int:
    """
    realize the function sqrt
    :param x: int
    :return: int
    """

# approach 1: binary search
    i = 0
    j = x
    while i <= j:
        mid = (i + j) // 2
        if mid ** 2 < x:
            i = mid + 1
        elif mid ** 2 > x:
            j = mid - 1
        else:
            return mid
    return j

# approach 2: newton iteration
# this is a fast way to fix function zero point


if __name__ == '__main__':

    print(mySqrt(4))