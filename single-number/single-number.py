class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = set()
        for n in nums:
            if n not in hashmap:
                hashmap.add(n)
            else:
                hashmap.remove(n)
        return list(hashmap)[0]