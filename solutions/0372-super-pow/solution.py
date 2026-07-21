class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        x=int(''.join(map(str,b)))
        return pow(a,x,1337)
