class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        prod=1
        num=n
        while True:
            x=num
            prod=1
            while x!=0:
                prod=prod*(x%10)
                x//=10
            if(prod%t==0):
                return num
            else:
                num+=1
            
