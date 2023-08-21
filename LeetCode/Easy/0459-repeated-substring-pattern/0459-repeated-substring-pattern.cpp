class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int n = s.size();
        for(int i=1; i<=n/2 ;i--){
            if(n%i==0){
                string sub = s.substr(0,i);
                string repeated = "";
                for(int j=0; j<n/i;j++)
                    repeated += sub;
                if(repeated == s)
                    return true;
            }
        }
        return false;
    }
};