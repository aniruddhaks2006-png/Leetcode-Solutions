class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        s=set()
        for i in range(len(nums)-2):
            if nums[i]==nums[i+1]==nums[i+2]:
                s.add(nums[i:i+3])
        if not s:
            return ""
        return max(s)
