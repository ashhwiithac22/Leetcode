class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num1 in nums1:
            if num1 in nums2:
                res.append(num1)
                nums2.remove(num1)
        return res

        