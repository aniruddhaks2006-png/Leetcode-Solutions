class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        a=[]
        b=[]
        for i in range(1,n+1):
            a.append(i)
        def search(a,c):
            if len(c)==k:
                b.append(c)
                return
            for i in range(len(a)):
                c.append(a[i])
                search(a[i+1:],c.copy())
                c.pop()
        search(a,[])
        return b
        
                
