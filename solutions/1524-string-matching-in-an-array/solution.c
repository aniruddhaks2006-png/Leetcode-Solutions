/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** stringMatching(char** words, int wordsSize, int* returnSize) {
    char **ans = (char **)malloc(wordsSize * sizeof(char *));
    int k = 0;

    for (int i = 0; i < wordsSize; i++) {
        for (int j = 0; j < wordsSize; j++) {
            if (i != j && strstr(words[j], words[i]) != NULL) {
                ans[k++] = words[i];
                break;  
            }
        }
    }

    *returnSize = k;
    return ans;
}
