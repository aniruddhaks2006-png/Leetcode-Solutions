class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
      b=[]
      for i in range(len(nums)):
          if(nums[i]==target):
              b.append(abs(i-start))
      return min(b)
              

