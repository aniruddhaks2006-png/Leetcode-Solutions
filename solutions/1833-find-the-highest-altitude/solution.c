int largestAltitude(int* gain, int gainSize) {
    int *a=(int*)malloc((gainSize+1)*sizeof(int));
    a[0]=0;
    for(int i=1;i<=gainSize;i++){
        a[i]=a[i-1]+gain[i-1];

    }
    int maxi=0;
    for(int i=0;i<=gainSize;i++){
        if(a[i]>maxi){
            maxi=a[i];

        }}
        return maxi;
    
}
