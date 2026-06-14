class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a2=[]
        a2.append(0)
        a2.append(gain[0])
        
        sum=gain[0]
        for i in range(1,len(gain)):
            sum+=gain[i]
            
            a2.append(sum)
        return max(a2)
        
        
        
