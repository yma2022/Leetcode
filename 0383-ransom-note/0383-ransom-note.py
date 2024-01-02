class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = Counter(magazine)
        
        for c in ransomNote:
            if c not in d:
                return False
            d[c] -= 1
            if d[c] == 0:
                del d[c]
                
        return True
        