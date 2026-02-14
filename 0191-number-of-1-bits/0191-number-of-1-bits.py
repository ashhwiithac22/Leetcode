class Solution(object):
    def hammingWeight(self, n):
        binary = format(n, 'b')
        count_1 = 0
        for bit in binary:
            if bit == '1':
                count_1 += 1
        return count_1
