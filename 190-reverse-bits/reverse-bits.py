class Solution(object):
    def reverseBits(self, n):
        binary = bin(n)[2:].zfill(32)
        reversed_string = binary[::-1]
        return int(reversed_string, 2)