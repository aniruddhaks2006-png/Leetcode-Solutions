class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        nums.sort()
        nums=set(nums)
        if len(nums)<3:
            return max(nums)
        l=list(nums)
        l.sort()
        return l[-3]
