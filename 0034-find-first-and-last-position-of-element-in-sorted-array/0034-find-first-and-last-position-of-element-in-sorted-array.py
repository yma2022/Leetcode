class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, val):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < val:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return left if nums[left] == val else -1
        
        def findRight(nums, val):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= val:
                    left = mid + 1
                else:
                    right = mid - 1 
            return right if nums[right] == val else -1
        
        if not nums or target > nums[-1] or target < nums[0]:
            return [-1, -1]
        left = findLeft(nums, target)
        right = findRight(nums, target)
        
        return [left, right]