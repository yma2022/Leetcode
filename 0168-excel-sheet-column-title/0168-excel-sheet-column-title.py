class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = []
        res = ""
        while columnNumber:
            s.append((columnNumber - 1) % 26)
            columnNumber = (columnNumber - 1) // 26
        for n in s[::-1]:
            res += chr(ord("A")+n)
            
        return res
        