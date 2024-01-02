class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds, dt = {}, {}
        for i, c in enumerate(s):
            if c not in ds and t[i] not in dt:
                ds[c] = t[i]
                dt[t[i]] = c
            elif c in ds and ds[c] == t[i]:
                continue
            elif t[i] in dt and dt[t[i]] == c:
                continue
            else:
                return False
                
        return True