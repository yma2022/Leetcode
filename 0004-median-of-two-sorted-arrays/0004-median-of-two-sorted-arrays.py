class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        if not nums1 or not nums2:
            merged = nums1 + nums2
            mid = len(merged) // 2
            return (merged[mid] + merged[mid - 1]) / 2 if len(merged)%2 == 0 else float(merged[mid])
      
        for i in range(len(nums1 + nums2)):
            if nums1[0] <= nums2[0]:
                merged.append(nums1.pop(0))
            else:
                merged.append(nums2.pop(0))
            if not nums1 or not nums2:
                break
        merged += nums1 + nums2
        print(merged)
        mid = len(merged) // 2
        res = len(merged) % 2
        if res == 0:
            return (merged[mid] + merged[mid - 1]) / 2
        else:
            return float(merged[mid])
        