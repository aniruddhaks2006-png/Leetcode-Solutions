
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l = len(s)
        j = 0
        lis = []
        for i in s:
            if i == "I":
                lis.append(j)
                j+=1
            else:
                lis.append(l)
                l-=1
        lis.append(l)        
        return lis
