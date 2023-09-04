class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        
        for i in range(cols):
            dp[0][i] = matrix[0][i]
            
        for i in range(1, rows):
            for j in range(cols):
                if j == 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
                elif j == cols - 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j]
                
        return min(dp[-1])
        
        
        