class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                if nums[mid] >= target >= nums[l]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid +1
                else:
                    r = mid
        return l if nums[l] == target else -1
        