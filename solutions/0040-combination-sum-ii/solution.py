class Solution:
    def combinationSum2(self,candidates:List[int],target:int)->List[List[int]]:
        candidates.sort()
        a=[]
        def search(b,sum,i):
            if sum==target:
                a.append(b.copy())
                return
            for k in range(i,len(candidates)):
                if k>i and candidates[k]==candidates[k-1]:
                    continue
                if sum+candidates[k]>target:
                    break
                search(b+[candidates[k]],sum+candidates[k],k+1)

        search([],0,0)
        return a
