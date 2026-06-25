class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for n in str(num):
            if num % int(n) == 0:
                count += 1
        return count
