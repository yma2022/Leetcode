class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        
        if sum_nums % 2 == 1:
            return False
        target = sum_nums // 2
        
        dp = [False] * (target + 1)
        dp[0] = True
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
                
        return dp[target]
        