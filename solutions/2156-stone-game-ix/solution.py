class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        tot=[0,0,0]
        for num in stones:
            tot[num%3]+=1
        if tot[0]%2==0:
            return tot[1]>0 and tot[2]>0
        return abs(tot[1]-tot[2])>2
  
