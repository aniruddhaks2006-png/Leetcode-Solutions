class Solution:
    def romanToInt(self, s: str) -> int:
        num=0
        i=0
        while i<len(s)-1:
            if s[i]=="C" and s[i+1] =="M":
                num=num+900  
                i+=1     
            elif s[i] =="M":
                num=num+1000
            elif s[i]=="C" and s[i+1] =="D":
                num=num+400
                i+=1
            elif s[i]=="D":
                num=num+500
            elif s[i]=="X" and s[i+1]=="C":
                num=num+90
                i+=1
            elif s[i]=="C":
                num=num+100
            elif s[i]=="X" and s[i+1]=="L":
                num=num+40
                i+=1
            elif s[i]=="L":
                num=num+50
            elif s[i]=="I" and s[i+1]=="X":
                num=num+9
                i+=1
            elif s[i]=="X":
                num=num+10
            elif s[i]=="I" and s[i+1]=="V":
                num=num+4
                i+=1
            elif s[i]=="V":
                num=num+5
            else:
                num=num+1
            i+=1
        if(i>len(s)-1):
            x=0    
        elif s[i] =="M":
                num=num+1000
            
        elif s[i]=="D":
                num=num+500
           
        elif s[i]=="C":
                num=num+100
            
        elif s[i]=="L":
                num=num+50
          
        elif s[i]=="X":
                num=num+10
            
        elif s[i]=="V":
                num=num+5
        else:
                num=num+1
        i+=1
        return num
