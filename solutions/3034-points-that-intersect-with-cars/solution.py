class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        x=[]
        for i in nums:
            for j in range(i[0],i[1]+1):
                x.append(j)
        l=list(set(x))
        return len(l)
        
