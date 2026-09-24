class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x=nums[i]
            b=0
            while x!=0:
                b+=x%10
                x//=10
            if b==i:
                return i
        return -1
