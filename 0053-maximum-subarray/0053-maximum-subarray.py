class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = maximum = nums[0]
        
        for num in nums[1:]:
            curr = max(num, curr + num)
            maximum = max(maximum, curr)
            
        return maximum