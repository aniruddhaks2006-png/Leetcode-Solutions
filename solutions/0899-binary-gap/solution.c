int binaryGap(int num) {
    int maxcount=0,count=0,numbeh=0;
    while(num>0){
        if((num%2)==1){
            
            if(numbeh && count+1>maxcount)
                maxcount=count+1;
            count=0;
            numbeh=1;
        }
        else if(numbeh){
            count++;
        }
           else
               count=0;
               
        
        num=num/2;
    }
    return maxcount;
}
