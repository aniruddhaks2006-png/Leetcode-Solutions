class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            s=set()
            total=0
            for j in range(i,len(nums)):
                total+=nums[j]
                s.add(nums[j])
                if total in s:
                    ans+=1
        return ans
