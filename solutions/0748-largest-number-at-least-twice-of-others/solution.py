class Solution:
    def dominantIndex(self, n: List[int]) -> int:
        if n==[]:
            return -1
        nums=sorted(n)
        
        if(nums[len(nums)-1]<2*nums[len(nums)-2]):
            return -1
        else:
            return n.index(nums[len(nums)-1])
