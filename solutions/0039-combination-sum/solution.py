class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def search(b,x,sum,target,i):
            if sum+x==target:
                b.append(x)
                a.append(b)
                return 1
            elif sum+x>target:
                return 0
            b.append(x)
            for k in range(i,len(candidates)):
                res=search(b.copy(),candidates[k],sum+x,target,k)
                if res==0:
                    continue
            return 1
        a=[]
        for i in range(len(candidates)):
            search([],candidates[i],0,target,i)
        return a

        
