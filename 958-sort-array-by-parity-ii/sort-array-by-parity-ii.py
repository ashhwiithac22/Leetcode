class Solution(object):
    def sortArrayByParityII(self, nums):
        n = len(nums)
        even = []
        odd = []
        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        nums[::2] = even
        nums[1::2] = odd
        return nums