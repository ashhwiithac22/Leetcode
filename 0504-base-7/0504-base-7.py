class Solution(object):
    def convertToBase7(self, num):
        if num == 0:
            return "0"
        sign = '-' if num < 0 else ""
        num = abs(num)
        ans = ""
        while num > 0:
            ans = str(num % 7) + ans
            num //= 7
        return sign + ans
