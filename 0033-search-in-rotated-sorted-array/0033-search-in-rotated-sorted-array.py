class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n =len(nums)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[r]:
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid                
            else:
                if target < nums[mid] and target >= nums[l]:
                    r = mid
                else:
                    l = mid + 1
                    
        return l if nums[l] == target else -1
                