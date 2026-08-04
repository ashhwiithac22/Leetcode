class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        arr = []
        mini = min(nums)
        maxi = max(nums)
        for i in range(mini, maxi):
            if i not in nums:
                arr.append(i)
        return arr