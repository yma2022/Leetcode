class Solution:
    def minFlips(self, target: str) -> int:
        res = 0
        for c in target:
            if res % 2 != int(c):
                res += 1
        return res