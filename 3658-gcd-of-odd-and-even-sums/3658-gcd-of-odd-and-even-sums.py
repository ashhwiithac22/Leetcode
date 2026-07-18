class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        osum = n * n 
        esum = n * (n + 1)
        rem = -1
        dividend = max(osum,esum)
        divisor = min(osum,esum)
        while divisor != 0:
            remainder = dividend % divisor
            dividend = divisor
            divisor = remainder
        return dividend


        
        