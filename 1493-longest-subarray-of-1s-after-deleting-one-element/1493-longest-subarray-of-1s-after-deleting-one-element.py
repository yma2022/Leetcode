class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        start = 0
        window = 0
        
        for i in range(len(nums)):
            zero_count += 1 if nums[i] == 0 else 0
            
            while zero_count > 1:
                zero_count -= 1 if nums[start] == 0 else 0
                start += 1
                
            window = max(window, i - start)
            
        return window
        