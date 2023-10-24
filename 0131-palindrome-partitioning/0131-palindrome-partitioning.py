class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        def backtrack(curr, path, results):
            if "".join(path) == s:
                results.append(path[:])
                return
            
            for i in range(curr, n):
                if isPalindrome(curr, i):
                    path.append(s[curr:i+1])
                    backtrack(i+1, path, results)
                    path.pop()
                    
        def isPalindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        res = []
        backtrack(0, [], res)
        return res
        