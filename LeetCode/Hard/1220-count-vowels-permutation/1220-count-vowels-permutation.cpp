#define ll long long
#define Modulo (ll)(1e9+7)
class Solution {
public:
    int countVowelPermutation(int n) {
        // Using a 2D vector to represent the 'dp' array
        vector<vector<ll>> dp(n, vector<ll>(5, 0));
        for (int i = 0; i < 5; ++i) {
            dp[0][i] = 1;
        }
        for (int i = 1; i < n; ++i) {
            dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][4]) % Modulo;
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % Modulo;
            dp[i][2] = (dp[i-1][1] + dp[i-1][3]) % Modulo;
            dp[i][3] = dp[i-1][2] % Modulo;
            dp[i][4] = (dp[i-1][2] + dp[i-1][3]) % Modulo;
        }

        int result = 0;
        for (int i = 0; i < 5; ++i) {
            result = (result + dp[n-1][i]) % Modulo;
        }
        return result;
    }
};