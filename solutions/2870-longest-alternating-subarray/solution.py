class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        for i in range(n - 1):
            if nums[i + 1] - nums[i] != 1:
                continue
            length = 2
            while i + length - 1 < n:
                expected = nums[i] + (length - 1) % 2
                if nums[i + length - 1] != expected:
                    break
                ans = max(ans, length)
                length += 1
        return ans
