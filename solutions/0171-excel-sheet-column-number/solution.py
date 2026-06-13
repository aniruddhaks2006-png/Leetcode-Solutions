class Solution:
    def titleToNumber(self, s: str) -> int:
        count=0
        for i in s:
           x=ord(i)-ord('A')
           count=count*26+x+1
        return count
            
        
        
