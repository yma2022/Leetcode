class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def searchLeft(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left if nums[left] == target else -1
        
        def searchRight(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right if nums[right] == target else -1
        
        if not nums or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        return [searchLeft(nums, target), searchRight(nums, target)]