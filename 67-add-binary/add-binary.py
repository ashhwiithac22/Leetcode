class Solution(object):
    def addBinary(self, a, b):
        sum1 = int(a, 2)+int(b, 2)
        return bin(sum1)[2:]


