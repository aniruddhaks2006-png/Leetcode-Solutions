class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        left=0
        ans=0
        d=Counter()
        distinct=0
        tot=len(set(nums))
        for right in range(len(nums)):
         d[nums[right]]+=1
         if d[nums[right]]==1:
                distinct+=1
         while tot==distinct:
            ans+=len(nums)-right
            d[nums[left]] -= 1
            if d[nums[left]] == 0:
                    distinct -= 1
            left += 1
        return ans


                  
