class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int,int> map;
        set<int> ans;
        int n = arr.size();
        for(int i=0; i<n; i++){
            map[arr[i]]++;
        }
        for(const auto& elem : map){
            ans.insert(elem.second);
        }
        return ans.size() == map.size() ? true:false;
    }
};