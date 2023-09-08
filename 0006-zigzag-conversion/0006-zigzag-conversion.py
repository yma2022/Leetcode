class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        ans = ""
        n = len(s)
        chars_in_section = 2 * (numRows - 1)
        
        for cur in range(numRows):
            index = cur
            while index < n:
                ans += s[index]
                
                if cur != 0 and cur != numRows - 1:
                    chars_in_between = chars_in_section - 2 * cur
                    second_index = index + chars_in_between
                    
                    if second_index < n:
                        ans += s[second_index]
                        
                index += chars_in_section
                
        return ans
        
        
        