class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a=[]
        b=[]
        for i in nums:
            if i>=0:
                a.append(i)
            else:
                b.append(i)
        k=0
        for i in range(0,len(nums),2):
            nums[i]=a[k]
            k+=1
        k=0
        for j in range(1,len(nums),2):
            nums[j]=b[k]
            k+=1
        return nums
