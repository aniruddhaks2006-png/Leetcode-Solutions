class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        if(len(nums)<2):
            return 0
        else:
            nums.sort()
            l=[]
            for i in range(len(nums)-1):
                l.append(abs(nums[i]-nums[i+1]))
        if(not l):
            return 0
        return max(l)
                
        
