from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cs=Counter(s)
        ct=Counter(t)
        ans=0
        for c in set(s+t):
            ans+=abs(cs[c]-ct[c])
        return ans
