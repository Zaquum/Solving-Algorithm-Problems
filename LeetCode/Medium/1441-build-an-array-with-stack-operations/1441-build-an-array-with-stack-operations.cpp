class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<int> s;
        vector<string> ans;
        for(int i=1; i<=n; i++){
            s.push_back(i);
            ans.push_back("Push");
            int last = s.size() - 1;
            if(target==s)
                break;
            if(target[last] != s[last]){
                ans.push_back("Pop");
                s.pop_back();
            }
        }
        return ans;
    }
};