class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for l in range(n):
            for r in range(l, n):
                arr = nums[:l] + nums[r+1:]

                if all(arr[i] < arr[i+1] for i in range(len(arr)-1)):
                    ans += 1

        return ans
