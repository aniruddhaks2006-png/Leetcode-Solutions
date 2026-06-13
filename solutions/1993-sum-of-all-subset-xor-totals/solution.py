class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sum=0
        x=len(nums)
        for i in nums:
            sum=sum | i
        return sum*2**(x-1)
        
