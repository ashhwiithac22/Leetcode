class Solution(object):
    def moveZeroes(self, nums):
        p = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        