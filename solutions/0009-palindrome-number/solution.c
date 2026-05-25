bool isPalindrome(int x) {
    long long num=0;
    int final;
    if(x>=0)
    {
    final=x;
    }
    else
    {
        return false;
}
    while(x!=0)
    {
    num=10*num+x%10;
    x=x/10;
    }
    if(num==final){
        return true;
    }
    return false;
}
    

