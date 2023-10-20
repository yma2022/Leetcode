class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        min_val = 0
        res = nums[0]
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
            min_val = min(min_val, nums[i-1])
            res = max(res, nums[i] - min_val)

        return res
        