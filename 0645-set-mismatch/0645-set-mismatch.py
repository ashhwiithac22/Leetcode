class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for num in nums:
            if nums.count(num)>1:
                duplicate = num
                break
        for i in range(1, len(nums)+1):
            if i not in nums:
                missing = i
                break
        return [duplicate,missing]

