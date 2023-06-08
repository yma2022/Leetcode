class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        left, right = 0, n - 1
        ans = -1
        while left < right:
            total = nums[left] + nums[right]
            if total >= k:
                right -= 1
            else:
                ans = max(ans, total)
                left += 1
        return ans