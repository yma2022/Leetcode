class Solution:
    def countOdds(self, low: int, high: int) -> int:
        d = high - low + 1
        r = low % 2 + d % 2
        count = d // 2 + 1 if r == 2 else d // 2
        return count