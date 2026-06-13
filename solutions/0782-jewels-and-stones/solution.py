class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        x=list(jewels)
        count=0
        for i in stones:
            if i in x:
                count+=1
        return count
