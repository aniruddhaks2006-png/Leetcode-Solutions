class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        ranges = []

        for num in nums:
            digits = str(num)
            maximum = max(digits)
            minimum = min(digits)

            ranges.append(int(maximum) - int(minimum))

        max_range = max(ranges)

        ans = 0
        for i in range(len(nums)):
            if ranges[i] == max_range:
                ans += nums[i]

        return ans

