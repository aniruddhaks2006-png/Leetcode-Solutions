class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        
        num3=[]
        for i in range(m):
        
            num3.append(nums1[i])

        
        for j in range(n):
            num3.append(nums2[j])
        
        
        num3.sort()
        for i in range(m+n):
         nums1[i]=num3[i]
     
        
        
