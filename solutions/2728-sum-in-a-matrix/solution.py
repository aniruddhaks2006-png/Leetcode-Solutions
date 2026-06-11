class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums:
            row.sort()
        ans = 0
        while nums[0]:
            mx = 0
            for row in nums:
                mx = max(mx, row.pop())
            ans += mx
        return ans
