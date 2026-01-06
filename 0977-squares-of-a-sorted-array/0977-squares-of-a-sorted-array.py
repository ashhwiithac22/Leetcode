class Solution(object):
    def sortedSquares(self, nums):
        list1 = []
        for num in nums:
            list1.append(num*num)
        return sorted(list1)