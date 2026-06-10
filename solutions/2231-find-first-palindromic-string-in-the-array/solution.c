bool pal(char *word){
   int left=0;
    int right=strlen(word)-1;
    while (left<right){
        if(word[left]!=word[right])
            return false;
        right--;
        left++;
    }
    return true;
    
    }

    
    char* firstPalindrome(char** words, int wordsSize) {
        for(int i=0;i<wordsSize;i++){
            if(pal(words[i])){
                return words[i];
            }
        }
        return "";
    
    
}
