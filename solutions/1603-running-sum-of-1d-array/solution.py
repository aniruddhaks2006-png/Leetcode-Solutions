class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        g=[]
        g.append(nums[0])
        for i in range(1,len(nums)):
            g.append(g[i-1]+nums[i])
        return g
            
