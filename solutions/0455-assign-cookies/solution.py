class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count=0
        i=0
        j=0
        g.sort()
        s.sort()
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                count+=1
                j+=1
                i+=1
            elif s[j]<g[i]:
                j+=1
        return count       
                
            
        
