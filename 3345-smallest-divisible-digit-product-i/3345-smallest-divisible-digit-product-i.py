class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n + 10):
            prod = 1
            for digit in str(i):
                prod *= int(digit)
            
            if prod % t == 0:
                return i
