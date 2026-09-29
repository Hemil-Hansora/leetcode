class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_buy = prices[0]

        for i in range(1, len(prices)):
            if min_buy > prices[i]:
                min_buy = prices[i]
            else:
                if max_profit < prices[i] - min_buy:
                    max_profit = prices[i] - min_buy

        return max_profit
