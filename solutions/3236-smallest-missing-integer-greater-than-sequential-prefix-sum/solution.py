class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        max=0
        r=1
        sume=nums[0]
    
        while r<len(nums) and nums[r]==nums[r-1]+1:
                sume+=nums[r]
                r+=1
        while sume in nums:
            sume+=1
        return sume


