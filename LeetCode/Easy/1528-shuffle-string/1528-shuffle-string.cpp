class Solution {
public:
    string restoreString(string s, vector<int>& indices) {
        int n = s.size();
        vector<char> tmp(n);
        for(int i=0; i<n; i++){
            tmp[indices[i]] = s[i];
        }
        string ans = "";
        for(auto& c : tmp)
            ans = ans + c;
        return ans;
    }
};