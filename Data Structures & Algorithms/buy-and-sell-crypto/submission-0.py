class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        count = 0
        next_counter = 1
        while next_counter < len(prices):
            low = prices[count]
            next_max_val = prices[next_counter]
            if low < next_max_val:
                profit = next_max_val - low
                max_profit = max(profit,max_profit)
            else:
                count = next_counter
            next_counter+=1

        return max_profit
        