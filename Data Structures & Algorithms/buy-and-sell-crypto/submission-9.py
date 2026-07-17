class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxP = 0

        while sell < len(prices):
            currP = prices[sell] - prices[buy]
            maxP = max(currP, maxP)

            if currP < 0:
                buy = sell
            sell += 1

        return maxP