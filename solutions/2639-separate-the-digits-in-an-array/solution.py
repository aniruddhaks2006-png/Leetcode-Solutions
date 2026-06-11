class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
      a=[]
      for i  in range(len(nums)-1,-1,-1):
        while nums[i]!=0:
            a.append(nums[i]%10)
            nums[i]//=10
      return a[::-1]
            
