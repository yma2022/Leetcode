class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        
        for i in range(len(nums)):
            if not dp[i]:
                continue
            for j in range(i, min(i+nums[i]+1, len(nums))):
                if dp[j]:
                    continue
                if j == len(nums) - 1:
                    return True
                dp[j] = True
        return dp[-1]
        