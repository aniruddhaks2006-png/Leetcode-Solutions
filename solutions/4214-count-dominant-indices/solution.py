class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        count = 0

        for i in range(len(nums)-1):
            if nums[i] > sum(nums[i+1:]) / (len(nums)-i-1):
                count += 1

        return count
