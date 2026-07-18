class Solution:
    def findGCD(self, nums: List[int]) -> int:
        dividend = max(nums)
        divisor = min(nums)
        while divisor != 0:
            remainder = dividend % divisor
            dividend = divisor
            divisor = remainder
        return dividend

        