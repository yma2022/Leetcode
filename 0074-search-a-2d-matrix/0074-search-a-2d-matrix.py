class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target > matrix[-1][-1] or target < matrix[0][0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m * n - 1
        
        while l <= r:
            mid = (l + r) // 2
            x, y = mid // n, mid - (mid // n) * n
            if matrix[x][y] >= target:
                r = mid - 1
            else:
                l = mid + 1
        x, y = l // n, l - (l // n) * n
        return matrix[x][y] == target
        