class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixMod = 0
        res = 0
        
        modGroups =[0 for _ in range(k)]
        modGroups[0] = 1
        
        for num in nums:
            prefixMod = (prefixMod + num%k) % k
            res += modGroups[prefixMod]
            modGroups[prefixMod] += 1
        return res