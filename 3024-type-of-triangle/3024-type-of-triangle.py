class Solution(object):
    def triangleType(self, nums):
        for i in range(len(nums)):
            if nums[i]+nums[i+1] <= nums[i+2] or nums[i]+nums[i+2]<= nums[i+1] or nums[i+1]+nums[i+2] <= nums[i]:
                return "none"
            if nums[i] == nums[i + 1] and nums[i+1] == nums[i+2]:
                return "equilateral"
            elif nums[i] == nums[i+1] or nums[i] == nums[i+2] or nums[i+1] == nums[i+2]:
                return "isosceles"
            else:
                return "scalene"
        return None