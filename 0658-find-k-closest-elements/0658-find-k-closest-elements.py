class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l, r = 0, n - k
        while l < r:
            mid = (l + r) // 2
            if arr[mid] - x < x - arr[mid+k]:
                l = mid + 1
            else:
                r = mid
        return arr[l:l+k]
        