bool wordBreak(char * s, char ** wordDict, int wordDictSize){
    int n = strlen(s);
    bool* memo = (bool*)malloc((n + 1) * sizeof(bool));
    memset(memo, false, (n + 1) * sizeof(bool));
    memo[0] = true;
    
    for(int i = 0; i <= n; i++){
        for(int j = 0; j < wordDictSize; j++){
            char* str = wordDict[j];
            int len = strlen(str);
            if(memo[i]){
                if(i + len <= n && strncmp(&s[i], str, len) == 0){
                    memo[i+len] = true;
                }
            }
        }
    }
    bool result = memo[n];
    free(memo);
    return result;
}