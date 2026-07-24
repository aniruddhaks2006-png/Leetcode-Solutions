from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        def cmp(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        nums.sort(key=cmp_to_key(cmp))
        ans = ''.join(nums)
        if ans[0] == '0':
            return '0'

        return ans

