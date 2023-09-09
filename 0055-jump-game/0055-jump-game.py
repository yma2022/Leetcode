class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        dp = [True] + [False] * (n - 1)
        
        for i in range(n):
            if not dp[i]:
                continue            
            for j in range(min(i + nums[i], n - 1), i, -1):
                if j == n - 1:
                    return True
                if dp[j]:
                    continue
                dp[j] = True
                
        return dp[-1]
        