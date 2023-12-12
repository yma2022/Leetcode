class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rows, cols = n, n
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        idx = 0
        
        row, col = 0, 0
        matrix = [[0] * cols for _ in range(rows)]
        
        for i in range(1, rows*cols+1):
            matrix[row][col] = i
            nextRow, nextCol = row + directions[idx][0], col + directions[idx][1]
            
            if not (0<=nextRow<rows and 0<=nextCol<cols and matrix[nextRow][nextCol] == 0):
                idx = (idx + 1) % 4
                
            row += directions[idx][0]
            col += directions[idx][1]
            
        return matrix