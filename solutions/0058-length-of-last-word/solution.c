int lengthOfLastWord(char* s) {
    int c=0,count=0;
    int n=strlen(s);
    for(int i=n-1;i>=0;i--)
    {
        if(count!=0 && s[i]==' ')
            break;
        else if(s[i]==' ')
            continue;
        else{
            c++;
            count=1;
        }             
    }
    return c;
}
