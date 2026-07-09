class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        maxProfit = 0

        while sell < len(prices):
            currProfit = prices[sell] - prices[buy]
            maxProfit = max(currProfit, maxProfit)

            if prices[buy] >= prices[sell]:
                buy = sell

            sell += 1

        return maxProfit
'''
        0  1  2  3  4  5
list = 10, 1, 5, 6, 7, 1

buy  = 1
sell = 2
curr = -9
max  = 0
'''