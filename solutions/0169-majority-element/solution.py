class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if(nums==[]):
            return 0
        nums.sort()
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        return max(d,key=d.get)
        
