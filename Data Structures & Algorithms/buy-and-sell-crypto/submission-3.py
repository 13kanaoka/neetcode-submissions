class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #loop through
        #compare each time where profit = max(currProfit, profit)
        #return profit at the end of loop

        #buy at index 0 (10) -> loop through each selling point and check if currProfit is greater than maxProfit
        #then buy at index 1 -> loop through ''

        maxProfit = 0
        for i in range(len(prices) - 1):
            currBuy = prices[i]

            for j in range(i + 1, len(prices)):
                currProfit = prices[j] - currBuy
                maxProfit = max(currProfit, maxProfit)

        return maxProfit