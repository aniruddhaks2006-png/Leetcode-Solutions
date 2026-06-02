class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        d={}
        for i in range(len(rectangles)):
         x=rectangles[i][0]/rectangles[i][1]
         if  x in d:
          d[x]+=1
         else:
            d[x]=1
        sum=0
        for i in d.keys():
            if(d[i]<2):
                continue 
            else:
                sum+=d[i]*(d[i]-1)//2
        return sum
