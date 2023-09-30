class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        if not s or not words:
            return 0
        count = 0
        for word in words:
            if self.stretchy(s, word):
                count += 1
        return count
    
    def stretchy(self, s, word):
        if not word:
            return False
        i, j = 0, 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                len1 = self.getRepeatedLength(s, i)
                len2 = self.getRepeatedLength(word, j)
                if len1 < 3 and len1 != len2 or len1 >= 3 and len1 < len2:
                    return False
                i += len1
                j += len2
            else:
                return False
        return i == len(s) and j == len(word)
    
    def getRepeatedLength(self, s, i):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        return j - i