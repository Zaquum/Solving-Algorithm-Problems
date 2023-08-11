int change(int amount, int* coins, int coinsSize){
    int dp[amount + 1];
    dp[0] = 1;
    for (int i = 1; i <= amount; i++) {
        dp[i] = 0; 
    }

    for(int i = 0; i < coinsSize; i++) {
        for(int j = coins[i]; j <= amount; j++) {
            if(j-coins[i]>=0)
                dp[j] += dp[j - coins[i]];
        }
    }

    return dp[amount];
}