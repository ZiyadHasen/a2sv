class Solution:
    def maxCoins(self, piles):
        piles.sort()
        res = 0
        n = len(piles)
        i = n // 3
        while i < n:
            res += piles[i]
            i += 2
        return res