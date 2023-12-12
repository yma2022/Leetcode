class Solution:
    def rob(self, nums: List[int]) -> int:
        amount = [0] * (len(nums)+1)
        amount[1] = nums[0]
        
        for i in range(2, len(nums) + 1):
            amount[i] = max(amount[i-2] + nums[i-1], amount[i-1])
            
        return amount[-1]
        