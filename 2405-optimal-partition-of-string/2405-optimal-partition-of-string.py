class Solution:
    def partitionString(self, s: str) -> int:
        lastseen = [-1] * 26
        count = 1
        start = 0
        
        for i in range(len(s)):
            if lastseen[ord(s[i]) - ord('a')] >= start:
                count += 1
                start = i
            lastseen[ord(s[i]) - ord('a')] = i
            
        return count
        