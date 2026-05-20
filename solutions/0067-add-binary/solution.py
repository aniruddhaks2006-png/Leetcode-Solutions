class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binary =a
        bind=b
        result1 = 0
        result2=0

        for bit in binary:
           result1 = result1 * 2 + int(bit)
        for bit in bind:
           result2 = result2 * 2 + int(bit)   
        final=result1+result2 
        return(bin(final)[2:])  


