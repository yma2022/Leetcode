class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        
        for i in range(n):
            if not dp[i]:
                continue
            for j in range(min(nums[i] + i, n - 1), i, -1):
                if j == n - 1:
                    return True
                if dp[j]:
                    continue
                dp[j] = True
        
        # print(dp)       
        return dp[-1]
        