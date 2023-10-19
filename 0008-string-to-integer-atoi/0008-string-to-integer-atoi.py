class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        ans = 0
        signal = None
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
            
        if i < len(s) and s[i] in ["+", "-"]:
            signal = s[i]
            i += 1
        
        while i < len(s) and s[i].isdigit():
            # print(signal, ans, s[i])
            if signal == "-" and (ans > -INT_MIN / 10 or (ans == -INT_MIN // 10 and int(s[i]) > 8)):
                return INT_MIN
            if signal != "-" and (ans > INT_MAX / 10 or (ans == INT_MAX // 10 and int(s[i]) > 7)):
                return INT_MAX
            ans = ans*10 + int(s[i])
            i += 1
                
        return -ans if signal == "-" else ans
            