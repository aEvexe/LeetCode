class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        l1 = []
        for i in range(len(accounts)):
            l1.append(sum(accounts[i]))

        l2 = sorted(l1, reverse=True)
        return l2[0]