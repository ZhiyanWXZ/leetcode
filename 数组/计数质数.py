def countPrimes(n: int) -> int:

    sum = 0
    for i in range(2, n):
        flag = True
        for j in range(2, i):
            if i % j == 0:
                flag = False
                break
        if flag is True:
            sum += 1
    return sum


if __name__ == "__main__":

    n = 10
    print(countPrimes(n))
