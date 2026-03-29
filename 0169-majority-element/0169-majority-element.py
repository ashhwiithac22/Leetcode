class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        seen = set()
        for num in nums:
            if num not in seen:
                if nums.count(num) > n/2:
                    return num
                seen.add(num)
                