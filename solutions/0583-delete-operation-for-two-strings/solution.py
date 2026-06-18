class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        storage=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    storage[i][j]=1+storage[i-1][j-1]
                else:
                    storage[i][j]=max(storage[i-1][j],storage[i][j-1])
        return m+n-2*storage[m][n]



        
