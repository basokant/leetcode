class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy, sell = 0, 1
        res = 0

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            res = max(res, profit)

            if prices[buy] > prices[sell]:
                buy += 1
            else:
                sell += 1

        return res
