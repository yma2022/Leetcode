class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        res = [""] * numRows
        curr = -1
        signal = 1
        
        for i in range(len(s)):
            if signal == 1:
                curr += 1
                res[curr] += s[i]
                if curr == numRows - 1:
                    signal = -1
            elif signal == -1:
                curr -=1
                res[curr] += s[i]
                if curr == 0:
                    signal = 1
                    
        print(res)    
        return "".join(res)
                
        
        
        