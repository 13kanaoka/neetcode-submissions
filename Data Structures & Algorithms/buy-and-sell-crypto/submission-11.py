class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l, r = 0, 1
        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            res = max(res, curr_profit)
            
            if curr_profit < 0:
                l = r
            r += 1

        return res