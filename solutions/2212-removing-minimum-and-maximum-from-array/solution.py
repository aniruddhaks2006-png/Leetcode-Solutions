class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 2:
            return n

        minidx = 0
        maxidx = 0
        maxi = float('-inf')
        mini = float('inf')

        for i in range(n):
            if nums[i] < mini:
                mini = nums[i]
                minidx = i

            if nums[i] > maxi:
                maxi = nums[i]
                maxidx = i

        left = max(minidx, maxidx) + 1
        right = n - min(minidx, maxidx)
        both = min(
            minidx + 1 + n - maxidx,
            maxidx + 1 + n - minidx
        )
        return min(left, right, both)
