class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        sum1=0
        sum2=0
        for b in range(k):
            sum1+=nums[i]
            i+=1
            sum2+=nums[j]
            j-=1
        return abs(sum1-sum2)

        
