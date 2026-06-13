class Solution:
    def canBeTypedWords(self, text: str, br: str) -> int:
        b=list(br)
        m=text.split()
        zup=0
        count=0
        for i in m:
            for j in b:
                if j in i:
                    count=-1
                    break
            if count!=-1:
                zup+=1
            count=0
        return zup
        
        
