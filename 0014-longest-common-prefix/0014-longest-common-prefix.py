class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for i in range(1,len(strs)):
            s = strs[i]
            n = min(len(prefix), len(s))
            if n == 0:
                return ""
            for j in range(n):
                if s[j] != prefix[j]:
                    prefix = prefix[:j]
                    print(prefix)
                    break
                else:
                    prefix = prefix[:n]
                    
        return prefix
                
            