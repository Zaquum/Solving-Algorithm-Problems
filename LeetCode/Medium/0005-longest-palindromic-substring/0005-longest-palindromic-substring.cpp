class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        vector<vector<bool>> dp(n, vector<bool>(n, false));
        for(int i=0; i<n; i++)
            dp[i][i] = true;
        string ans = string(1, s[n-1]);

        int maxLen = 1;
        for(int lo = n-1; lo > -1; lo--){
            for(int hi = lo+1; hi < n; hi++){
                if(s[lo] == s[hi]){
                    if(hi - lo == 1 or dp[lo+1][hi-1]){
                        dp[lo][hi] = true;
                        if(maxLen < hi - lo + 1){
                            maxLen = hi - lo + 1;
                            ans = s.substr(lo, maxLen);
                        }
                    }
                }
            }
        }
        return ans;
    }
};