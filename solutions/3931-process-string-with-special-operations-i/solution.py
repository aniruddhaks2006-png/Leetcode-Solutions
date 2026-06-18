class Solution:
    def processStr(self, s: str) -> str:
        a=[]
        for i in s:
            if i>="a" and i<="z":
                a.append(i)
            elif i =="#":
                a=a+a
            elif i=="%":
                a=a[::-1]
            elif i=="*":
                a=a[:-1]
            else:
                continue
        s=""
        for i in a:
            s+=i
        return s
