class Solution:
    def minOperations(self, nums: List[int]) -> int:
        i=0
        count=0
        while i<len(nums)-1:
            if nums[i+1]<=nums[i]:
                count+=nums[i]-nums[i+1]+1
                nums[i+1]+=nums[i]-nums[i+1]+1
                
                
            else:
                i+=1
        return count
        
