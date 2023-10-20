class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        
        for i in range(n):
            for j in range(i+1, min(n, i + nums[i] + 1)):
                if not dp[j]:
                    dp[j] = dp[i] + 1
                else:
                    dp[j] = min(dp[j], dp[i] + 1)
                # print(dp)
        return dp[-1]
        
        