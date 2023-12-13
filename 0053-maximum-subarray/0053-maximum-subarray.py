class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        
        minVal = None
        total = 0
        
        for i in range(len(nums)):
            total += nums[i]
            if not minVal:
                dp[i] = total                
                minVal = total
            else:
                dp[i] = max(total - minVal, total)
                minVal = min(minVal, total)
                
        return max(dp)
        