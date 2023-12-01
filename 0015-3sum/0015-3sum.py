class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                while i+1 < l < n and nums[l] == nums[l-1]:
                    l += 1
                while 0 < r < n-1 and nums[r] == nums[r+1]:
                    r -= 1
                if l < r and nums[l] + nums[r] + nums[i] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif l < r and nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                elif l < r and nums[l] + nums[r] + nums[i] < 0:
                    l += 1
        return res
                
        