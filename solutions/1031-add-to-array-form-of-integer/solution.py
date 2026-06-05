class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
       sum=0
       for i in num:
           sum=10*sum+i
       sum=sum+k
       l=[]
       while sum>0:
           l.append(sum%10)
           sum=sum//10
       if l==[]:
           return []
       l=l[::-1]
       while l[0]==0:
           l.remove(l[0])
       return l
