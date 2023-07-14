int longestSubsequence(int* arr, int arrSize, int difference){
    int dp[20001] = {0};
    int offset = 10000; // to handle negative numbers in the array
    int max_length = 0;
    for (int i = 0; i < arrSize; ++i) {
        int num = arr[i] + offset;
        if (num - difference >= 0 && num - difference <= 20000) {
            dp[num] = dp[num - difference] + 1;
        } else {
            dp[num] = 1;
        }
        if (dp[num] > max_length) {
            max_length = dp[num];
        }
    }
    return max_length;
}