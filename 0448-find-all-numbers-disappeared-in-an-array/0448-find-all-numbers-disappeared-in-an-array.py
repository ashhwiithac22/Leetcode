class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        disappeared = []
        for i in range(1, len(nums)+1):
            if i not in s:
                disappeared.append(i)
        return disappeared