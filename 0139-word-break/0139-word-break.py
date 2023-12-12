class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        canSeg = [False] * (len(s) + 1)
        canSeg[0] = True
        
        for i in range(len(s) + 1):
            if not canSeg[i]:
                continue
            for j in range(i+1, len(s) + 1):
                if s[i:j] in wordDict:
                    canSeg[j] = True
                    
        return canSeg[-1]
        