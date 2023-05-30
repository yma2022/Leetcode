class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i = 0
        j = 0
        m = len(mat)
        n = len(mat[0])
        res = []
        while i < m and j < n:
            res.append(mat[i][j])
            # print(i, j)
            if (i + j) % 2 == 0:
                if i == 0 and j < (n-1):
                    j += 1
                elif j == (n-1):
                    i += 1
                else:
                    i -= 1
                    j += 1
            else:
                if j == 0 and i < (m-1):
                    i += 1
                elif i == (m-1):
                    j += 1
                else:
                    i += 1
                    j -= 1
        return res
                
            
        