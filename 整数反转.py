
class Solution:
    def reverse(self, x):
        result = ""
        quotation = abs(x)
        if quotation == 0:

            return 0
        while quotation != 0:
            # 负数求余以前还真没注意过
            reminder = quotation % 10
            # print(reminder)
            quotation = int(quotation / 10)

            result += str(reminder)
        result = int(result)
        # print(result)
        if result > 2**31-1:

            return 0
        if x < 0:
            if -result < -2**31:

               return 0
            result = -result
        return result
if __name__ == '__main__':
    s = Solution()
    a = s.reverse(0)
    print(a)