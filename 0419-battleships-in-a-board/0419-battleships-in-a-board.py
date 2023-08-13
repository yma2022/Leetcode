class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(x, y, d):
            if visited[x][y]:
                return
            visited[x][y] = True           
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                if board[nx][ny] == 'X' and not visited[nx][ny]:
                    dfs(nx, ny, d)
                        
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and not visited[i][j]:
                    d = [0, 0]
                    for dx,dy in [[0,1], [0,-1], [1,0], [-1,0]]:
                        if 0 <= i+dx < len(board) and 0 <= j+dy < len(board[0]):
                            if board[i + dx][j + dy] == 'X':
                                d = [dx, dy]
                    count += 1
                    dfs(i, j, d)
                    
        return count