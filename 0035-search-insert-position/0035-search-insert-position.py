class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        n = len(nums)
        right = n - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return left if nums[left] >= target else left + 1