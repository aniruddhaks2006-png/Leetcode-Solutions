class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        j=0
        i=0
        ans=0
        while i<len(nums1) and j<len (nums2):
            if nums2[j]>=nums1[i]:
                ans=max(ans,j-i)
                j+=1
            else:
                i+=1
        return ans
        
        
