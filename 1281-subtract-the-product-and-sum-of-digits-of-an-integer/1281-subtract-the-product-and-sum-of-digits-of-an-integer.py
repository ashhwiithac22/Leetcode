class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum_digit = 0
        for num in str(n):
            product *= int(num)
            sum_digit += int(num)
        return product - sum_digit

        