class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        cols = len(matrix[0])
        rows = len(matrix)
        
        visited = [[False] * cols for _ in range(rows)]
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        idx = 0
        order = [0] * (rows*cols)
        
        row, col = 0, 0
        for i in range(rows*cols):
            order[i] = matrix[row][col]
            visited[row][col] = True
            nextRow, nextCol = row + directions[idx][0], col + directions[idx][1]
            
            if not (0<=nextRow<rows and 0<=nextCol<cols and not visited[nextRow][nextCol]):
                idx = (idx + 1) % 4
            
            row = row + directions[idx][0]
            col = col + directions[idx][1]
            
        return order
        