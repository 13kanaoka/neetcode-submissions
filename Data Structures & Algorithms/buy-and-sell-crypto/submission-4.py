class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        for i in range(len(prices) -1):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                curr_profit = prices[j] - buy
                max_profit = max(curr_profit, max_profit)

        return max_profit