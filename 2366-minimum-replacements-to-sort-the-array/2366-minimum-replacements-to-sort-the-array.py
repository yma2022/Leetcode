class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue
            count = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
            
            ans += count - 1
            
            nums[i] = nums[i] // count
            
        return ans
                
        