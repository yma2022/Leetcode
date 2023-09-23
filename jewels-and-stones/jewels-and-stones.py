class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = set(list(jewels))
        res = 0
        for s in stones:
            if s in d:
                res += 1
        return res
        