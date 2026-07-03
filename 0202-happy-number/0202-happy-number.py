class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            square_sum = 0
            while n > 0:
                last_digit = n % 10
                square_sum += last_digit * last_digit
                n //= 10
            n = square_sum
        return True
        


         
        