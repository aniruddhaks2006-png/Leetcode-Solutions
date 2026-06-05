class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        x = None
        y = None
        if len(nums) == 2:
            return [nums[0], nums[1]]
        if nums[0] != nums[1]:
            x = nums[0]
        for i in range(1, len(nums) - 1):
            if nums[i - 1] != nums[i] and nums[i] != nums[i + 1]:
                if x is None:
                    x = nums[i]
                else:
                    y = nums[i]
        if nums[-1] != nums[-2]:
            if x is None:
                x = nums[-1]
            else:
                y = nums[-1]
        return [x, y]
