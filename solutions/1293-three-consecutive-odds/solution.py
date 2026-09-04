class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        l=0
        r=0
        while r<len(arr):
            if arr[r]%2!=0:
                r+=1
            else:
                l=r+1
                r=r+1
            if r-l==3:
                return True
        return False
