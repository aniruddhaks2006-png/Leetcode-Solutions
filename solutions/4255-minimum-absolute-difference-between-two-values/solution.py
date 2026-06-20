class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
     mini=0
     mixi=len(nums)
     if 1 in nums and 2 in nums:
          for i in range(len(nums)):
              for j in range(len(nums)):
               if nums[i]==1 and nums[j]==2:
                mini=abs(i-j)
                if mini<mixi:
                   mixi=mini
             
          return mixi  
     else: 
           return -1
