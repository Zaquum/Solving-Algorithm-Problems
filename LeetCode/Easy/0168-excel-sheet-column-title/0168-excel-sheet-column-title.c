char * convertToTitle(int columnNumber){
    char *result = (char *)malloc(10 * sizeof(char));
    int idx = 0;
    
    while(columnNumber > 0) {
        columnNumber--;
        result[idx++] = (columnNumber % 26) + 'A';
        columnNumber /= 26;
    }
    
    result[idx] = '\0'; // Null-terminating the string.

    for (int i = 0; i < idx / 2; i++) {
        char temp = result[i];
        result[i] = result[idx - i - 1];
        result[idx - i - 1] = temp;
    }
    
    return result;
}