class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp=[[float('inf')]*(i+1) for i in range(rowIndex+1)]
        dp[0][0]=1
        for x in range(1,rowIndex+1):
        
              dp[x][0]=1
              dp[x][x]=1
        for i in range(2,rowIndex+1):
            for j in range(1,i):
                dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
        return dp[rowIndex]
        
