class Solution:
    def maximumTime(self, time: str) -> str:
        time=list(time)
        t=""
        for i in  range(len(time)):
            if time[i]=="?":
                if i==0 and time[i+1]>"3" and time[i+1]!="?" :
                    time[i]="1"
                elif i==0:
                    time[i]="2"
                elif i==1 and time[i-1]=="2":
                    time[i]="3"
                elif i==1:
                    time[i]="9"
                elif i==3:
                    time[i]="5"
                elif i==4:
                    time[i]="9"
                else:
                    continue
        return t.join(time)
