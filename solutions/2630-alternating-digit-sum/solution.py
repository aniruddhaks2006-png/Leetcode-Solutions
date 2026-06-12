class Solution:
    def alternateDigitSum(self, n: int) -> int:
        j=0
        s=0
        for i in list(str(n)):
            s+=int(i)*((-1)**j)
            j+=1
        return s

        
