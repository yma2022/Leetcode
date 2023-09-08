class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1, numRows+1):
            temp = [0] * i
            temp[0], temp[-1] = 1, 1
            for j in range(1,i-1):
                temp[j] = res[-1][j-1] + res[-1][j]
            res.append(temp)
            
        return res
        