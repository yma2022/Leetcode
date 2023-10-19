class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        ans = 0
        val = abs(x)
        while val > 0:
            pop = val % 10
            val //= 10
            if x > 0 and (ans > INT_MAX / 10 or (ans == INT_MAX // 10 and pop > 7)):
                return 0
            if x < 0 and (ans > -INT_MIN / 10 or (ans == -INT_MIN // 10 and pop > 8)):
                #print(ans)
                return 0
            
            ans = ans * 10 + pop
        return ans if x > 0 else -ans
        