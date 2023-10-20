class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0 for _ in range(9)] for _ in range(9)]
        cols = [[0 for _ in range(9)] for _ in range(9)]
        units = [[0 for _ in range(9)] for _ in range(9)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j])
                unit_idx = (i // 3) * 3 + j // 3
                if rows[i][num - 1] > 0 or cols[j][num - 1] > 0 or units[unit_idx][num - 1] > 0:
                    return False
                rows[i][num - 1] = 1
                cols[j][num - 1] = 1
                units[unit_idx][num - 1] = 1
        return True
        