class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        a=[[1 for s in range(n)] for _ in range(n)]
        top=0
        right=n-1
        left=0
        bottom=n-1
        k=1
        while top<=bottom and left<=right:
            for x in range(left,right+1):
                a[top][x]=k
                k+=1
            top+=1
            for x in range(top,bottom+1):
                a[x][right]=k
                k+=1
            right-=1
            for x in range(right,left-1,-1):
                a[bottom][x]=k
                k+=1
            bottom-=1
            for x in range(bottom,top-1,-1):
                a[x][left]=k
                k+=1
            left+=1
        return a

        
