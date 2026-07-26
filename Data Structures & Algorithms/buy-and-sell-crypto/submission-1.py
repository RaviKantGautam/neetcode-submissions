class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxprofit = 0
        for price in prices:
            minPrice = min(price, minPrice)
            maxprofit = max(maxprofit, price - minPrice)
        return maxprofit