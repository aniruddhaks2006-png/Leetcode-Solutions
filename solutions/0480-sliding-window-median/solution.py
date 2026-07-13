from bisect import bisect_left, insort

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])
        ans = []
        for i in range(k, len(nums) + 1):
            if k % 2:
                ans.append(float(window[k // 2]))
            else:
                ans.append((window[k // 2 - 1] + window[k // 2]) / 2)
            if i == len(nums):
                break
            window.pop(bisect_left(window, nums[i - k]))
            insort(window, nums[i])

        return ans
