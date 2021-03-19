
#  return False if x < 0 else (x == int(str(x)[::-1]))
# s[a:b:c]: advanced usage， 对 s 中的在 a 和 b 之间的元素以 c 为间隔切片。 c 值如果为负，则会进行反向取值。
def isPalindrome(x):
    """
    Palindrome: 回文数
    :param x:
    :return:
    """
    if x < 0:
        return False
    result = ""
    if x == 0:
        return True
    quotient = x
    while quotient != 0:
        reminder = quotient % 10
        quotient = int(quotient / 10)

        result += str(reminder)
    # print(result)
    if x == int(result):
        return True
    else:
        return False

if __name__ == "__main__":
   print(isPalindrome(1001))