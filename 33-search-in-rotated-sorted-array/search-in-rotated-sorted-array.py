class Solution(object):
    def search(self, nums, target):
        for num in nums:
            if target in nums:
                return nums.index(target)
        return -1
        