class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        int cur = 0;
        vector<int> ans;
        for(auto &num : pref){
            int elem = cur^num;
            ans.push_back(elem);
            cur = cur^elem;
        }
        return ans;
    }
};