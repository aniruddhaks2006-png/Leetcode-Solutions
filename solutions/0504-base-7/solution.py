class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        symbol1=0
        if num<0:
            num=-num
            symbol1=1
            
        sum=""
        while num!=0:
            sum=sum+str(num%7)
            num=num//7
        if symbol1:
         sum=sum+"-"
        else:
            x=0
        return sum[::-1]
        
