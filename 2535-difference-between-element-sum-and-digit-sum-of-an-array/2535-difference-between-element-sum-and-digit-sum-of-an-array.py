class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        el_sum = 0
        di_sum =0
        for el in nums:
            el_sum += el
            for digit in str(el):
                di_sum += int(digit)

        return abs(el_sum - di_sum)
        