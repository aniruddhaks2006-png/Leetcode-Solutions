class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
         a=[]
         for i in nums1:
           count=0
           for j in range(nums2.index(i),len(nums2)):
                 if nums2[j]>i:
                    a.append(nums2[j])
                    count=1
                    break
           if count==0:
               a.append(-1)
           
            
         return a
        
