class Solution(object):
    def findPeakElement(self, nums):
        nums = [float('-inf')] + nums+ [float('-inf')]
        n = len(nums)
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                return i - 1
        return -1