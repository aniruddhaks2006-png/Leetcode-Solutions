class Solution:
    def checkDivisibility(self, n: int) -> bool:
        prod=1
        sumi=0
        x=n
        while n!=0:
            y=n%10
            sumi+=y
            prod*=y
            n//=10
        if x%(sumi+prod)!=0:
            return False
        return True
