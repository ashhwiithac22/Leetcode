class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(1, 110):
            multiple = k * i
            if multiple not in nums:
                return multiple


            