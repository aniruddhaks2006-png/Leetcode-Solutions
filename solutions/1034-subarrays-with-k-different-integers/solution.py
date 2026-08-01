from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def f(k):
            d=defaultdict(int)
            l=c=0
            for r,x in enumerate(nums):
                d[x]+=1
                while len(d)>k:
                    d[nums[l]]-=1
                    if d[nums[l]]==0:
                        del d[nums[l]]
                    l+=1
                c+=r-l+1
            return c
        return f(k)-f(k-1)
