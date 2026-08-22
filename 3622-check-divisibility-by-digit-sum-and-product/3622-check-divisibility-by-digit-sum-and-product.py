class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        prod_sum = 1
        for i in str(n):
            digit_sum += int(i)
            prod_sum *= int(i)

        sum1 = digit_sum + prod_sum
        if n % sum1 == 0:
            return True
        else:
            return False 
        