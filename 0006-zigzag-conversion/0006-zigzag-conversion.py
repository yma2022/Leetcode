class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [[] for _ in range(numRows)]
        flag = 1
        currRow = 0
        for i in range(len(s)):
            if i > 0 and i % (numRows - 1) == 0:
                flag *= -1
            res[currRow].append(s[i])
            currRow += flag
            
        ans = ""
        for i in range(numRows):
            ans += "".join(res[i])
        return ans
        