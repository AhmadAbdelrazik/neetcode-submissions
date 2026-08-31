class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            f = {}
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] in f:
                    return False
                
                f[board[i][j]] = True
        
        for i in range(9):
            f = {}
            for j in range(9):
                if board[j][i] == ".":
                    continue
                
                if board[j][i] in f:
                    return False
                
                f[board[j][i]] = True
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                f = {}
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] == ".":
                            continue

                        if board[i+k][j+l] in f:
                            return False
                        
                        f[board[i+k][j+l]] = True


        return True