class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(curr, addr, res):
            if "".join(addr) == s and len(addr) == 4:
                res.append(".".join(addr))
                return
            for i in range(curr, len(s)):
                if isValid(curr, i):
                    addr.append(s[curr:i+1])
                    backtrack(i+1, addr, res)
                    addr.pop()
                
                
        def isValid(start, end):
            if s[start:end+1].isdigit():
                if start != end and s[start] == "0":
                    return False
                if 0 <= int(s[start:end+1]) <= 255:
                    return True
            else:
                return False
        
        results = []
        backtrack(0, [], results)
        return results
        