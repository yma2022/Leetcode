class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = m - 1
        for i in range(m//2):
            for j in range((m+1)//2):
                matrix[i][j], matrix[n - j][i],matrix[n-i][n-j],matrix[j][n-i] = matrix[n - j][i],matrix[n-i][n-j],matrix[j][n-i], matrix[i][j]