class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap1 = dict()
        hashmap2 = dict()
        ans = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum = nums1[i] + nums2[j]
                if sum in hashmap1:
                    hashmap1[sum] += 1
                else:
                    hashmap1[sum] = 1
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                sum = - nums3[i] - nums4[j]
                if sum in hashmap2:
                    hashmap2[sum] += 1
                else:
                    hashmap2[sum] = 1
        for key in hashmap1:
            if hashmap1[key] and key in hashmap2:
                ans += hashmap1[key] * hashmap2[key]
        return ans