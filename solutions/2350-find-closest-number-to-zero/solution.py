class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in nums:
            if abs(i) < abs(ans):
                ans = i
            elif abs(i) == abs(ans) and i > ans:
                ans = i
        return ans
