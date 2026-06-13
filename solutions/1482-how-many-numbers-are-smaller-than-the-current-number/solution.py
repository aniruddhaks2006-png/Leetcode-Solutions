class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=sorted(nums)
        g=[]
        for i in range(len(nums)):
            g.append(l.index(nums[i]))
        return g
        
