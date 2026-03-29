class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        sorted_even = []
        for num in nums:
            if num % 2 == 0:
                sorted_even.append(num)
        unique = []
        for num1 in sorted_even:
            if sorted_even.count(num1) == 1:
                unique.append(num1)
        if unique:
            return unique[0]
        return -1