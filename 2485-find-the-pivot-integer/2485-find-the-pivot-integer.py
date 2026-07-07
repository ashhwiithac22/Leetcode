class Solution:
    def pivotInteger(self, n: int) -> int:
        for x in range(1, n + 1):
            left_sum = 0
            for num in range(1, x + 1):
                left_sum += num
            right_sum = 0
            for num in range(x, n + 1):
                right_sum += num

            if left_sum == right_sum:
                return x
        return -1        

        