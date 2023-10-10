class Solution:
    res = 0
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        size = len(s)
        for i in range(1, size):
            self.res += self.A(10, i) - self.A(9, i - 1)
        visited = [0] * 10
        self.dfs(s, 0, visited)
        return self.res
    def dfs(self, s, i, visited):
        n = len(s)
        if (i >= n):
            self.res += 1
            return
        for j in range(10):
            if j == 0 and i == 0:
                continue
            if visited[j] == 1:
                continue
            if j < int(s[i]):
                self.res += self.A(10 - i -1, n - 1 - i)
            elif j == int(s[i]):
                visited[j] = 1
                self.dfs(s, i+1, visited)
                visited[j] = 0
    def A(self, m, k):
        if (k==0):
            return 1;        
        res = 1;
        for i in range(k):
            res *= (m-i);
        return res;