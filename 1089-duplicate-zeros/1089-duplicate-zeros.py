class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        result = []
        for num in arr:
            if num == 0:
                result.append(0)
                result.append(0)
            else:
                result.append(num)
        arr[:] = result[:len(arr)]