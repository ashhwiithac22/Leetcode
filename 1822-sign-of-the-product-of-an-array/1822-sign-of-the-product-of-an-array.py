class Solution(object):
    def arraySign(self, nums):
        result = 1
        for num in nums:
            result = result * num
        if result == 0:
            return 0
        elif result > 1:
            return 1
        else:
            return -1
        