class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        l=0
        r=1
        maxxprofit=0
        while r<len(nums):
            if nums[r]>nums[l]:
                profit=nums[r]-nums[l]
                if profit>maxxprofit:
                    maxxprofit=profit
            else:
                l=r
            r+=1
        return maxxprofit
        
