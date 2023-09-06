class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        lastDay = days[-1]
        dp = [0] * (lastDay + 1)
        
        index = 0
        for i in range(lastDay + 1):
            if i < days[index]:
                dp[i] = dp[i - 1]
            else:
                index += 1
                dp[i] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
                
        return dp[-1]
        