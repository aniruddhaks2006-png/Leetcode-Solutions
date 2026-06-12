class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1=0
        sum2=0
        for j in nums:
            sum1+=j
            while j!=0:
                sum2+=j%10
                j//=10
        
    
        return abs(sum1-sum2)
        
