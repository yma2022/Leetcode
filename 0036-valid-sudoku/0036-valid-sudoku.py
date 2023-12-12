class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        units = [set() for _ in range(9)]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j])
                unit_idx = (i // 3) * 3 + j // 3
                if num in rows[i] or num in cols[j] or num in units[unit_idx]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                units[unit_idx].add(num)
        return True