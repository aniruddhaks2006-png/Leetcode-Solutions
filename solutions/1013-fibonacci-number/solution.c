

int fib(int n){
    if(n<=0)
        return 0;
    if(n==1)
        return 1;
    int temp,great=1;
    int sum=0;
    
 for(int i=2;i<=n;i++){
     
     temp=great+sum;
     sum=great;
     great=temp;
     
 }
    return temp;
}
