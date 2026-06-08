bool detectCapitalUse(char* word) {
    int get=0;
    if(word[0]>=65 && word[0]<=90)
        get=1;
    int count=0;
    int cap=0;
    for(int i=0;i<strlen(word);i++){
        if(word[i]>=65 && word[i]<=90){
            count++;
        }
        else{
            cap++;
        }
    }
    if(cap>0 && cap==strlen(word)){
            return true;
        }
    if(get==1 && cap==strlen(word)-1)
        return true;
    if(count>0 && count==strlen(word))
        return true;
    return false;
    
}
