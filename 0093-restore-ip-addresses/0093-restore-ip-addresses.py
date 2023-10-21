class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(curr, path, results):
            if "".join(path[:]) == s and len(path) == 4:
                results.append(".".join(path[:]))
                return
            
            for i in range(curr, len(s)):
                if not s[curr:i+1] or int(s[curr:i+1]) > 255:
                    continue
                if s[curr:i+1][0] == "0" and len(s[curr:i+1])>1:
                    continue
                path.append(s[curr:i+1])
                backtrack(i+1, path, results)
                path.pop()           
            
        res = []
        backtrack(0, [], res)
        return res
        