class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        b=[1,2,3,4,5,6,7,8,9]
        def search(s,sumi,so):
            if sumi==n:
                if len(so)==k:
                    a.append(so)
                    return 0
            if not s:
                return None
            if len(so)>=k:
                return 0
            for i in range(len(s)):
                if sumi +s[i]>n:
                    break
                else:
                    so.append(s[i])
                    search(s[i+1:],sumi+s[i],so.copy())
                    so.pop()
        a=[]
        for i in range(len(b)):
                if b[i]>n:
                    break
                else:
                    search(b[i+1:],b[i],[b[i]])
        return a


        
