# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:        
    def binarySearchPeak(self, mountain_arr) -> int:
        left, right = 0, mountain_arr.length() - 1
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        return left

    def binarySearchAscending(self, mountain_arr, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < target:
                left = mid + 1
            else:
                right = mid
        return left if mountain_arr.get(left) == target else -1

    def binarySearchDescending(self, mountain_arr, left, right, target):
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) > target:
                left = mid + 1
            else:
                right = mid
        return left if mountain_arr.get(left) == target else -1

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        size = mountain_arr.length()
        peek_i = self.binarySearchPeak(mountain_arr)

        res_left = self.binarySearchAscending(mountain_arr, 0, peek_i, target)
        res_right = self.binarySearchDescending(mountain_arr, peek_i + 1, size - 1, target)
        
        return res_left if res_left != -1 else res_right