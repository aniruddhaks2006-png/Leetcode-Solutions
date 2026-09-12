class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        a=[[None for p in range(len(s))] for _ in range(numRows)]
        k=0
        left=0
        bottom=numRows-1
        while k<len(s):
            for p in range(numRows):
                if k==len(s):
                    break
                a[p][left]=s[k]
                k+=1
            for p in range(numRows-2):
                if k==len(s):
                    break
                bottom-=1
                left+=1
                a[bottom][left]=s[k]
                k+=1
            left+=1
            bottom=numRows-1
        si=""
        for row in a:
            for x in row:
                if x is not None:
                    si+=x
        return si




