class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n
        nums.sort()
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > mid:
                right = mid
            else:
                left = mid + 1

        return nums[left] - 1 if left < n else nums[right - 1] + 1

        