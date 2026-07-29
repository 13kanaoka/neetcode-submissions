class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        buy, sell = 0, 1

        while sell < len(prices):
            currProfit = prices[sell] - prices[buy]
            maxProfit = max(currProfit, maxProfit)

            if currProfit < 0:
                buy = sell
            sell += 1

        return maxProfit