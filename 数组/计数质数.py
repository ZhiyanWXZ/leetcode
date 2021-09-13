import math


# 暴力
def countPrimes(n: int) -> int:

    sum = 0
    for i in range(2, n):
        flag = True
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                flag = False
                break
        if flag is True:
            sum += 1
    return sum


# 埃氏筛
def countPrimes_EthierSieve(n: int) -> int:
    # isPrime = [0 for _ in range(n)]
    isPrime = [1] * n
    for i in range(n):
        if i == 0 or i == 1:
            isPrime[i] = 0
            continue
        if isPrime[i] == 1:
            for j in range(i*i, n, i):
                isPrime[j] = 0
    return sum(isPrime)


if __name__ == "__main__":

    n = 20

    print(countPrimes_EthierSieve(n))
