class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            m = {}
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in m:
                    return False
                m[board[i][j]] = True

        for i in range(9):
            m = {}
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in m:
                    return False
                m[board[j][i]] = True
        
        for i in range(9):
            m = {}
            for j in range(9):
                r = j // 3 + 3 * (i // 3)
                c = j % 3 + 3 * (i % 3)
                if board[r][c] == ".":
                    continue
                elif board[r][c] in m:
                    return False
                m[board[r][c]] = True
        
        return True