class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Binary search
        # n = len(arr)
        # left = 0
        # right = n - k
        # while left < right:
        #     mid = left + (right - left) // 2
        #     if x - arr[mid] > arr[mid + k] - x:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return arr[left: left + k]
        
        # Two pointers
        n = len(arr)
        left = 0
        right = n - 1
        while right - left >= k:
            if abs(arr[right] - x) >= abs(x - arr[left]):
                right -= 1
            else:
                left += 1
        return arr[left: right + 1]

                