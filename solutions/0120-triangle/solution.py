class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[[float('inf')]*(i+1) for i in range(len(triangle))]
        dp[0][0]=triangle[0][0]
        for x in range(1,len(triangle)):
        
              dp[x][0]=dp[x-1][0]+triangle[x][0]
              dp[x][x]=dp[x-1][x-1]+triangle[x][x]
        for i in range(2,len(triangle)):
            for j in range(1,i):
                dp[i][j]=triangle[i][j]+min(dp[i-1][j],dp[i-1][j-1])
        return min(dp[len(triangle)-1])
        
