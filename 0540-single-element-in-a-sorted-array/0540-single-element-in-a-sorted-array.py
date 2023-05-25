class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if (mid % 2 == 0 and nums[mid] == nums[mid-1]) or (mid % 2 != 0 and nums[mid] == nums[mid+1]):
                right = mid - 1
            elif (mid % 2 != 0 and nums[mid] == nums[mid-1]) or (mid % 2 == 0 and nums[mid] == nums[mid+1]):
                left = mid + 1
            else:
                return nums[mid]
                
                
        return nums[left]