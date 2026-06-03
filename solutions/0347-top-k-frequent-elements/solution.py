class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if(nums==[]):
            return []
        
        nums.sort()
        d={}
        l=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in range(k):
            x=max(d,key=d.get)
            l.append(x)
            del d[x]
        return l
            
