class Solution(object):
    def maximumWealth(self, accounts):
        result = []
        for account in accounts:
            account_sum = 0
            for num in account:
                account_sum += num
            result.append(account_sum)
        return max(result)
        