class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations.reverse()
        count=0
        for i in citations:
            if i>=count+1:
                count+=1
            else:
                
                return count
       
            
        return  count
