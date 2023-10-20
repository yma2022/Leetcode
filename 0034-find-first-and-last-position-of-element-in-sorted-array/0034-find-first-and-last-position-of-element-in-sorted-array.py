class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            n = len(nums)
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            return l if nums[l] == target else -1
        def findRight(nums, target):
            n = len(nums)
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return r if nums[r] == target else -1
        
        if not nums or target > nums[-1] or target < nums[0]:
            return [-1, -1]
        left = findLeft(nums, target)
        right = findRight(nums, target)
        print(left, right)
        return[left, right]