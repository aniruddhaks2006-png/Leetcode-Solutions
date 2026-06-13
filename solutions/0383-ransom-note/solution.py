class Solution:
    def canConstruct(self, ran: str, mag: str) -> bool:
        l=list(ran)
        g=list(mag)
        x=len(g)
        for i in l:
            if i in g:
             g.remove(i)
        if len(g)==x-len(l):
            return True
        return False
