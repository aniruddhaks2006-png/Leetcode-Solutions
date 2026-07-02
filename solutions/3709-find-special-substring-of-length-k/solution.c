bool hasSpecialSubstring(char* s, int k) {
    if (s == NULL)
        return k == 0;
    char a = s[0];
    if (s[1] == '\0') {
        if (k == 1)
            return true;
        return false;
    }
    int count = 1;
    for (int i = 1; s[i] != '\0'; i++) {
        if (a == s[i]) {
            count++;
        } else {
            if (count == k)
                return true;
            count = 1;
            a = s[i];
        }
    }
    if (count == k)  
        return true;
    return false;
}
