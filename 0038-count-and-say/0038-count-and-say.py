class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n - 1)
        ans = ""
        cur = prev[0]
        count = 1
        for i in range(1, len(prev)):
            if prev[i] != cur:
                ans += str(count) + str(cur)
                cur = prev[i]
                count = 1
            else:
                count +=1
        if count != 0:
            ans += str(count) + str(cur)
        return ans
        