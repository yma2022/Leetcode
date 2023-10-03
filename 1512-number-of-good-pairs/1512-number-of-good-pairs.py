class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)
        ans = 0
        for num in nums:            
            ans += d[num]
            d[num] += 1
        return ans