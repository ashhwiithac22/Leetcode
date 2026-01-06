class Solution(object):
    def removeDuplicates(self, nums):
        arr = []
        for num in nums:
            if num in arr:
                continue
            else:
                arr.append(num)
        for i in range(len(arr)):
             nums[i] = arr[i]
        return len(arr)

        