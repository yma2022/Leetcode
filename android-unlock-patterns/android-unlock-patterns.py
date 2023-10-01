class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        def dfs(seen, skip, cur, remain):
            if remain < 0 :
                return 0
            if remain == 0:
                return 1
            seen[cur] = True
            rst = 0
            for i in range(1,10):
                if not seen[i] and (skip[cur][i] == 0 or seen[skip[cur][i]]):
                    rst += dfs(seen, skip, i, remain - 1)
            seen[cur] = False
            return rst
        
        skip = [[0 for _ in range(10)] for _ in range(10)]
        skip[1][3] = skip[3][1] = 2;
        skip[1][7] = skip[7][1] = 4;
        skip[3][9] = skip[9][3] = 6;
        skip[7][9] = skip[9][7] = 8;
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5;
        seen = [False] * 10
        rst = 0
        for i in range(m, n + 1):
            rst += dfs(seen, skip, 1, i - 1) * 4;    # 1, 3, 7, 9 are symmetric
            rst += dfs(seen, skip, 2, i - 1) * 4;    # 2, 4, 6, 8 are symmetric
            rst += dfs(seen, skip, 5, i - 1);        # 5
        return rst