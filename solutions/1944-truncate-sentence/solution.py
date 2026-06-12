class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        si=""
        m=s.split(" ")
        count=0
        for i in m:
            if count<k:
                si+=i+" "
                
                count+=1
            else:
                break
        return si[:-1]
            
        
