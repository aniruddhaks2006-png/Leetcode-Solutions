class Solution:
    def simplifyPath(self, path: str) -> str:
        s=[]
        m=path.split("/")
        for i in m:
            if i==".":
                continue
            elif i=="":
                continue
            elif i=="..":
                if s!=[]:
                    s.pop()
            else:
                s.append(i)
        str="/"
        for i in s:
            str+=i+"/"
        if len(str)==1:
            return str
        return str[:-1]


        
