#include <stdbool.h>
#include <string.h>
#include <ctype.h>

bool isPalindrome(char* s) {

    int left = 0;
    int right = strlen(s) - 1;

    while (left < right) {

        // move left to valid char
        while (left < right && !isalnum(s[left])) {
            left++;
        }

        // move right to valid char
        while (left < right && !isalnum(s[right])) {
            right--;
        }

        // compare (case-insensitive)
        if (tolower(s[left]) != tolower(s[right])) {
            return false;
        }

        left++;
        right--;
    }

    return true;
}
