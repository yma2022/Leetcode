class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        threeSum = float('inf')
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                while l < r and l > i + 1 and nums[l] == nums[l-1]:
                    l += 1
                while l < r and r < n - 1 and nums[r] == nums[r+1]:
                    r -= 1
                total = nums[i] + nums[l] + nums[r]
                if abs(total - target) < abs(threeSum - target):
                    threeSum = total
                if l < r and total == target:
                    return target
                elif l < r and total > target:
                    r -= 1
                else:
                    l += 1
                    
        return threeSum
            
        