class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        a = [["0" for _ in range(9)] for _ in range(9)]
        b = [["0" for _ in range(9)] for _ in range(9)]
        c = [["0" for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                box=(i//3)*3+j//3
                if board[i][j]!="." and (board[i][j] in a[i] or board[i][j] in b[j] or board[i][j] in c[box]) :
                    return False
                a[i][j]=board[i][j]
                b[j][i]=board[i][j]
                c[box][i%3*3+j%3]=board[i][j]
        return True
