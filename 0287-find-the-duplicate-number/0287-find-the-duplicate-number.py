class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l - (l - r) // 2
            if nums[mid] <= mid:
                r = mid - 1
            else:
                l = mid + 1
        return nums[l]
        