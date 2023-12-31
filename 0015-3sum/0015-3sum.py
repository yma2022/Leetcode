class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)
        for i in range(n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if l < r and total == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif l < r and total > 0:
                    r -= 1
                elif l < r and total < 0:
                    l += 1
        return res
                    
                
        
        