class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        
        for i in range(n):
            if not dp[i]:
                continue
            for j in range(i+1, min(n, i+nums[i]+1)):
                if dp[j]:
                    continue
                if j == n-1:
                    return True
                dp[j] = True
        return dp[-1]
        