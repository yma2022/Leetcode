class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = [-1] * 26
        for i in range(len(s)):
            if d[ord(s[i]) - ord('a')] != -2 and d[ord(s[i]) - ord('a')] != -1:
                d[ord(s[i]) - ord('a')] = -2
            elif d[ord(s[i]) - ord('a')] == -1:
                d[ord(s[i]) - ord('a')] = i
        print(d)
        index = float('inf')
        for n in d:
            if n >= 0:
                index = min(index, n)
        return index if max(d) >= 0 else -1
            
        