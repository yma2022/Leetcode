class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        start, end = 0, 1
        prefix = s[0]
        curr = 1
        while curr < n:
            if prefix[start] != s[curr]:
                curr = end
                end += 1                
                prefix = s[:end]
                start = 0

            else:
                start += 1
                start = start % len(prefix)
            curr += 1
            #print(prefix)
        return len(s) % len(prefix) == 0 and len(prefix) < len(s)
               
            
        