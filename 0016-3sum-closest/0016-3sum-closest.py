class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = inf
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                if abs(sum3 - target) < abs(ans - target):
                    ans = sum3
                if sum3 < target:
                    left += 1
                else:
                    right -= 1
        return ans
                
        