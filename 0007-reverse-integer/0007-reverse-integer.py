class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        INTMAX = 2**31 - 1
        INTMIN = -2**31
        val = abs(x)
        while val:
            pop = val % 10
            val = val // 10
            if rev > INTMAX / 10 or (rev == INTMAX / 10 and pop > 7):
                return 0
            if rev < INTMIN or (rev == INTMIN / 10 and pop < -8):
                return 0
            rev = rev*10 + pop
        return rev if x>0 else -rev