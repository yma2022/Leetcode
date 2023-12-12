class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                length[i] = max(length[i], length[j]+1)
        # print(length)         
        return max(length)
        