class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(b, w, x, y):
            if len(w) == 0:
                return True
            if x<0 or x>=m or y<0 or y>=n or w[0] != b[x][y]:
                return False
            tmp = b[x][y]
            b[x][y] = "#"
            res = dfs(b,w[1:],x+1,y) or dfs(b,w[1:],x-1,y) or dfs(b,w[1:],x,y+1) or dfs(b,w[1:],x,y-1)
            b[x][y] = tmp
            return res
            
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(board, word, i, j):
                        return True
        return False