class Solution(object):
    def minimumCost(self, nums):
        first = nums[0]
        rest = nums[1:]
        rest.sort()
        second = rest[0]
        third = rest[1]
        return first + second + third
