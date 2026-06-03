class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        si=""
        s=list(s)
        for i in t:
            if i in s:
                s.remove(i)
                continue
            if i not in s:
                si+=i
        return si
        
        
