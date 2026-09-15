class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m=len(board)
        n=len(board[0])

        directions=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        for i in range(m):
            for j in range(n):
                count=0

                for di,dj in directions:
                    x=i+di
                    y=j+dj

                    if 0<=x<m and 0<=y<n:
                        if board[x][y]==1 or board[x][y]==2:
                            count+=1

                if board[i][j]==1:
                    if count<2 or count>3:
                        board[i][j]=2
                else:
                    if count==3:
                        board[i][j]=3
        for i in range(m):
            for j in range(n):
                if board[i][j]==2:
                    board[i][j]=0
                elif board[i][j]==3:
                    board[i][j]=1
