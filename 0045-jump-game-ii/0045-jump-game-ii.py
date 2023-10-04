class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        
        dp[0] = 0
        
        for i in range(len(nums)):
            for j in range(min(i + nums[i], len(nums) - 1), i, -1):
                dp[j] = min(dp[j], dp[i] + 1)
        # print(dp)
        return dp[-1]
        