class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        rowSet = set()
        colSet = set()
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)
                    
        for row in rowSet:
            matrix[row] = [0] * cols
            
        for col in colSet:
            for i in range(rows):
                matrix[i][col] = 0
        