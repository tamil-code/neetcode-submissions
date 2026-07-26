class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')
        max_profit = float('-inf')
        for price in prices:
            min_val = min(price,min_val)
            profit = price-min_val
            max_profit = max(profit,max_profit)
        return max_profit