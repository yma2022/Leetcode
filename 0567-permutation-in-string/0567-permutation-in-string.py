class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = collections.Counter(s1)
        k = len(s1)
        for i in range(len(s2)):  # ---- O(n)
            sub = s2[i:i+k]  # ------ O(k)
            d2 = collections.Counter(sub) # --- O(k)
            if d1 == d2:
                return True
        return False        