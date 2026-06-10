char* replaceDigits(char* s) {
    for(int i=0;i<strlen(s)-1;i+=2){
        s[i+1]=s[i]+s[i+1]-'0';
    }
    return s;
}
