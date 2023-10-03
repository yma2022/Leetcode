class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ""
        ops = None
        for ch in s:
            if ch == " " and not ans and not ops:
                continue
            if not ch.isdigit() and ch not in ["-", "+"]:
                break
            if ch in ["-", "+"]:
                if ops or ans:
                    break
                else:
                    ops = ch
            if ch.isdigit():
                ans += ch
        if not ans:
            return 0
        ans = -int(ans) if ops == "-" else int(ans)
        if ans < -2**31:
            return -2**31
        elif ans > 2**31 - 1:
            return 2**31 - 1
        else:
            return ans
        