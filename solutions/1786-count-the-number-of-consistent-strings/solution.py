class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        x=list(allowed)
        count=0
        all=0
        for i in words:
            for j in i:
                if j not in x:
                    count=-1
                    break
            if count!=-1:
                all+=1
            count=0
        return all
                
