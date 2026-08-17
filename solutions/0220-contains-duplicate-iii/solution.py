from bisect import insort, bisect_left

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        s = []

        for r in range(len(nums)):
            # Remove elements that are too far away in index
            if r > indexDiff:
                old = nums[r - indexDiff - 1]
                pos = bisect_left(s, old)
                s.pop(pos)

            # Find a value >= nums[r] - valueDiff
            pos = bisect_left(s, nums[r] - valueDiff)

            # Check if that value is also <= nums[r] + valueDiff
            if pos < len(s) and s[pos] <= nums[r] + valueDiff:
                return True

            # Add current number
            insort(s, nums[r])

        return False

