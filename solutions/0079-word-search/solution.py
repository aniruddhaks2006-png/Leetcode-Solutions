class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        def search(r,c,i):
            if i==len(word):
                return True
            if r<0 or r>=row or c<0 or c>=col or board[r][c]!=word[i]:
                return False
            temp=board[r][c]
            board[r][c]='#'
            found=search(r-1,c,i+1)+search(r,c-1,i+1)+search(r+1,c,i+1)+search(r,c+1,i+1)
            board[r][c]=temp
            return found
        for x in range(len(board)):
            for y in range(len(board[0])):
                if search(x,y,0):
                    return True
        return False
            
