class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        d={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}
        d1 = { 0:"0",1:"1",2:"2",3:"3",4:"4",5:"5", 6:"6",7:"7",8:"8",9: "9"}
        sum1=0
        sum2=0
        for i in num1:
            sum1=10*sum1+d[i]
        for i in num2:
            sum2=10*sum2+d[i]
        s=sum1+sum2
        if s==0:
            return  "0"
        sti=""
        while(s!=0):
            i=s%10
            s=s//10
            sti+=d1[i]
        sup=sti[::-1]
        return sup
        
