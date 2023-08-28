class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m * n - 1
        
        def getIndex(n, col):
            if n % col == 0:
                i = n // col - 1
            else:
                i = n // col
            j = n - i * col - 1
            return (i, j)
        
        while left < right:
            mid = (left + right) // 2
            i, j = getIndex(mid+1, n)
            if matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid
                
        i_final, j_final = getIndex(left+1, n)
        return matrix[i_final][j_final] == target