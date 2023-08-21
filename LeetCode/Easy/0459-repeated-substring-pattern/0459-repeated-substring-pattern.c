bool repeatedSubstringPattern(char * s){
    int n = strlen(s);
    for (int i = n / 2; i >= 1; i--) {
        if (n % i == 0) {
            char *sub = (char *)malloc(i + 1);
            strncpy(sub, s, i);
            sub[i] = '\0';
            char *repeated = (char *)malloc(n + 1);
            repeated[0] = '\0';
            for (int j = 0; j < n / i; j++) {
                strcat(repeated, sub);
            }
            if (strcmp(repeated, s) == 0) {
                free(sub);
                free(repeated);
                return true;
            }
            free(sub);
            free(repeated);
        }
    }
    return false;
}