class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        gap = 0
        for i in range(1, len(nums)):
            gap = max(nums[i]-nums[i-1], gap)
            
        return gap