int scoreOfString(char* s) {
    int temp=s[0]-'a';
    int i=0;
    int ans=0;
    while(s[i]!='\0'){
        ans+=abs(s[i]-'a'-temp);
        temp=s[i]-'a';
        i++;
    }
    return ans;
}
