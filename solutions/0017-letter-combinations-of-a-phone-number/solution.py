class Solution:
    def letterCombinations(self, digit: str) -> List[str]:
        if len(digit)==0:
            return []
        a=[]
        s=""
        def search(digit,i,s):
            d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
            if(i==len(digit)-1):
                for x in range(len(d[digit[i]])):
                    a.append(s+d[digit[i]][x])
                return None
            for x in range(len(d[digit[i]])):
                    search(digit,i+1,s+d[digit[i]][x])
        search(digit,0,"")
        return a



