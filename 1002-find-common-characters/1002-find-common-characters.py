class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []
        hashmap = [0] * 26
        ans = []
        for c in words[0]:
            hashmap[ord(c) - ord("a")] += 1
        for i in range(1, len(words)):
            hashOther = [0] * 26
            for c in words[i]:
                hashOther[ord(c) - ord("a")] += 1
            for j in range(26):
                hashmap[j] = min(hashmap[j], hashOther[j])
        
        for i in range(26):
            while hashmap[i]:
                ans.append(chr(i + ord("a")))
                hashmap[i] -= 1
        return ans
            
        