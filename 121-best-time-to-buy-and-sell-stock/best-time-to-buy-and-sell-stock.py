class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        localMin = prices[0]
        profit = 0

        for price in prices:
            if price < localMin:
                localMin = price
            else:
                profit = max(profit, price - localMin)
            
        return profit
        