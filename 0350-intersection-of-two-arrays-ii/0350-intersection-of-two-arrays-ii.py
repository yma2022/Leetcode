class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = list()
        hashmap = dict()
        for num in nums1:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
                
        for num in nums2:
            if num in hashmap:
                if hashmap[num] > 0:
                    hashmap[num] -= 1
                    res.append(num)
        return res        