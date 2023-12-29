class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = Counter(s)
        center = False
        for key in d:
            if d[key] % 2 == 1 and center:
                return False
            if d[key] % 2 == 1 and not center:
                center = True
            else:
                continue
        return True