class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum1 = []
        sum2 = []
        for num in nums:
            if num < 10:
                sum1.append(num)
            else:
                sum2.append(num)
        alice_sum = 0
        bob_sum = 0
        for a in range(len(sum1)):
            alice_sum += sum1[a]
        for b in range(len(sum2)):
            bob_sum += sum2[b]
        if alice_sum > bob_sum or bob_sum > alice_sum:
            return True
        else:
            return False        