class Solution:
    def generate(self,row: int) -> List[List[int]]:
        dp=[[float('inf')]*(i+1) for i in range(row)]
        dp[0][0]=1
        for x in range(1,row):
        
              dp[x][0]=1
              dp[x][x]=1
        for i in range(2,row):
            for j in range(1,i):
                dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
        return dp
        
        
