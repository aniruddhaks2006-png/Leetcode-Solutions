class Solution:
    def countAsterisks(self, s: str) -> int:
        count=1
        sike=0
        for i in s:
            if i=="|":
                count=-count
            if i=="*" and count!=-1:
                sike+=1
        return sike
               
                
        
