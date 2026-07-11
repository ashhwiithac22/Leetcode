class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            rev = str(-x)
            ans = -int(rev[::-1])
        else:
            rev = str(x)
            ans = int(rev[::-1])

        if ans < -2 ** 31 or ans > 2 ** 31:
            return 0
        
        return ans