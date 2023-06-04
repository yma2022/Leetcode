class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = [0, 0], [m-1, n-1]
        while left[0] * n + left[1] < right[0] * n + right[1]:
            mid = [(n * (left[0] + right[0]) + left[1] + right[1]) // (2 * n), ((n * (left[0] + right[0]) + left[1] + right[1]) // 2) %  n]
            if matrix[mid[0]][mid[1]] < target:
                left[0] = mid[0] + (mid[1] + 1) // n
                left[1] = (mid[1] + 1) % n
            else:
                right = mid
        return matrix[left[0]][left[1]] == target