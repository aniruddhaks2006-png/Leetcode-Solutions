bool isSumEqual(char* firstWord, char* secondWord, char* targetWord) {
    int sum1=0,sum2=0,sum3=0;
    for(int i=0;i<strlen(firstWord);i++){
        sum1=10*sum1+(firstWord[i]-'a');
    }
    for(int i=0;i<strlen(secondWord);i++){
        sum2=10*sum2+(secondWord[i]-'a');
    }
    for(int i=0;i<strlen(targetWord);i++){
        sum3=10*sum3+(targetWord[i]-'a');
    }
    if(sum1+sum2==sum3)
        return true;
    return false;
}
