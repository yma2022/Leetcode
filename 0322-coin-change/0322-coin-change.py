class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = [-1] * (amount + 1)
        count[0] = 0
        
        for i in range(1, amount + 1):
            if i < min(coins):
                count[i] = -1
                continue
            for c in coins:
                if i < c or count[i - c] == -1:
                    continue
                if count[i] == -1:
                    count[i] = count[i-c] + 1
                else:
                    count[i] = min(count[i], count[i-c] + 1)
        #print(count)     
        return count[-1] 
        