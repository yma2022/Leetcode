class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(curr, part, res):
            if "".join(part) == s:
                res.append(part[:])
                return
            
            for i in range(curr, len(s)):
                if isPalindrome(curr, i):
                    part.append(s[curr:i+1])
                    backtrack(i+1, part, res)
                    part.pop()
                    
        def isPalindrome(start, end):
            i, j = start, end
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        results = []
        backtrack(0, [], results)
        return results
        