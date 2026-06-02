char* reversePrefix(char* word, char ch) {
    int x=0;
    int j=0;
    int temp;
    if(strlen(word)==0 || strlen(word)==1)
        return word;
    for(int i =0;i<strlen(word);i++)
    {
        if(word[i]==ch){
            x=i;
            break;
        }
    }
    while(j<x)
    {
        temp=word[j];
        word[j]=word[x];
        word[x]=temp;
            j++;
        x--;
    }
    return word;
    
}
