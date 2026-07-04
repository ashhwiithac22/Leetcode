class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        lucky = -1
        for num in freq:
            if num == freq[num]:
                if num > lucky:
                    lucky = num
        return lucky      