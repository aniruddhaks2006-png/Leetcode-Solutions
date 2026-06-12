class Solution:
    def minElement(self, nums: List[int]) -> int:
        sum=0
        mini=nums[0]
        for i in nums:
            while i!=0:
                sum+=i%10
                i//=10
            if(sum<mini):
                mini=sum
            sum=0
        return  mini
