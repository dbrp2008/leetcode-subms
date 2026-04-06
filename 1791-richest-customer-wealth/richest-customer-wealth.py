class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        most = 0
        for i in range(0, len(accounts)):
            x = sum(accounts[i])
            if x > most:
                most = x
        return most