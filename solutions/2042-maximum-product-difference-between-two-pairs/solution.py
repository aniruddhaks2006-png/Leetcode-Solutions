class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        firstmin=float('inf')
        secondmin=float('inf')
        firstmax=float('-inf')
        secondmax=float('-inf')
        for s in nums:
            if s<firstmin:
                secondmin=firstmin
                firstmin=s
            elif s<secondmin:
                secondmin=s
            if s>firstmax:
                secondmax=firstmax
                firstmax=s
            elif s>secondmax:
                secondmax=s
        if secondmin==float('inf') or secondmax==float('-inf'):
             return 0
        return (firstmax*secondmax)-(firstmin*secondmin)
