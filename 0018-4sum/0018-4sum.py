class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j + 1, n - 1
                while l < r:
                    while l < r and l > j + 1 and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and r < n - 1 and nums[r] == nums[r + 1]:
                        r -= 1
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if l < r and total == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif total > target:
                        r -= 1
                    else:
                        l += 1
        return res
                    
        