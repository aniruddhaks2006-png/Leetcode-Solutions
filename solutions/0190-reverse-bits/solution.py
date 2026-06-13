class Solution:
    def reverseBits(self, n: int) -> int:
        s=bin(n)
        s=s[2:]
        s=s.zfill(32)
        sup=0
        s=s[::-1]
        for i in s:
            sup=sup*2+int(i)
        return sup
            

        
    
        
        
        
