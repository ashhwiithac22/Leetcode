class Solution:
    def sumAndMultiply(self, n: int) -> int:
        n = str(n)
        x = ""
        for num in n:
            if num != '0':
                x += num
        if x == "":
            return 0
        sum1 = 0
        for num in x:
            sum1 += int(num)
        return int(x)*sum1
        