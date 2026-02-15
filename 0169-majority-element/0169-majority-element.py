class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        checked = set()
        for num in nums:
            if num not in checked:
                if nums.count(num) > n/2:
                    return num
                checked.add(num)