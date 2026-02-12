class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        lastseen = {}
        for i in range(len(nums)):
            if nums[i] in lastseen:
                distance = i - lastseen[nums[i]]
                if distance <= k:
                    return True
            lastseen[nums[i]] = i
        return False