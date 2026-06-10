#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* digitSum(char* s, int k) {
    while (strlen(s) > k) {
        char *newStr = (char *)malloc(strlen(s) * 2 + 1);
        newStr[0] = '\0';

        int i = 0;
        while (s[i] != '\0') {
            int sum = 0;
            for (int j = 0; j < k && s[i] != '\0'; j++, i++) {
                sum += s[i] - '0';
            }

            char temp[10];
            sprintf(temp, "%d", sum);
            strcat(newStr, temp);
        }
        s = newStr;
    }
    return s;
}
