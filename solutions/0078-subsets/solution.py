class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        b=set()
        def subset(a,c):
            b.add(tuple(c))
            for i in range(len(a)):
                c.append(a[i])
                subset(a[i+1:],c.copy())
                c.pop()
        subset(nums,[])
        return list(b)
        
