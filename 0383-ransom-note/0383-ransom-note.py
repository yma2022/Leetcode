class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = [0] * 26
        for c in magazine:
            hashmap[ord(c) - ord("a")] += 1
        
        for c in ransomNote:
            if hashmap[ord(c) - ord("a")] > 0:
                hashmap[ord(c) - ord("a")] -= 1
            else:
                return False
        return True
        