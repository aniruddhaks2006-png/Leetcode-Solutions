int twoEggDrop(int n) {
    int i=0;
    int sum=0;
    while(sum<n){
        sum=i*(i+1)/2;
        i++;
    }
    if(i==0)
        return 0;
    return i-1;
}
