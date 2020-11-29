class Solution:
    def maximumWealth(self, accounts) -> int:
        return max([sum(account) for account in accounts])
