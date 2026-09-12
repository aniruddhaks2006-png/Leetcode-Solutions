class Solution:
    def minRemoveToMakeValid(self,s:str)->str:
        si=""
        stu=[]
        rem=set()

        for i in range(len(s)):
            if s[i]=="(":
                stu.append(i)
            elif s[i]==")":
                if stu:
                    stu.pop()
                else:
                    rem.add(i)

        for i in stu:
            rem.add(i)

        for i in range(len(s)):
            if i not in rem:
                si+=s[i]

        return si
