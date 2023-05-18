class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p_buy = p_sell = 0
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] > prices[p_sell]:
                p_sell = i
                max_profit = max(prices[p_sell] - prices[p_buy], max_profit)
            elif prices[i] < prices[p_buy]:
                p_buy = i
                p_sell = i
            else:
                pass
        return max_profit