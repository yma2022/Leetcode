class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = m - 1
        q = n - 1
        
        for i in range(len(nums1) - 1, -1, -1):
            if p >= 0 and q >= 0:
                if nums2[q] > nums1[p]:
                    nums1[i] = nums2[q]
                    q -= 1
                else:
                    nums1[p], nums1[i] = nums1[i], nums1[p]
                    p -= 1
            elif p >= 0:
                nums1[p], nums1[i] = nums1[i], nums1[p]
                p -= 1
            elif q >= 0:
                nums1[i] = nums2[q]
                q -= 1
        
            
        