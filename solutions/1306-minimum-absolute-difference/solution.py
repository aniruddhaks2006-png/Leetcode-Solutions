class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mi=2e6+1
        c=[]
        j=[]
        for i in range(len(arr)-1):
            c.append(abs(arr[i]-arr[i+1]))
        if min(c)>mi:
            return []
        else:
         mi=min(c)
        for i in range(len(arr)-1):
            if(abs(arr[i]-arr[i+1])==mi):
                j.append([arr[i],arr[i+1]])
        return j
        
