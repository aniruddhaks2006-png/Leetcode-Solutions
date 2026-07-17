class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l=0
        r=int(sqrt(c))
        while l<=r:
            prod=l*l+r*r
            if prod==c:
                return True
            elif prod>c:
                r-=1
            else:
                 l+=1
        return False
