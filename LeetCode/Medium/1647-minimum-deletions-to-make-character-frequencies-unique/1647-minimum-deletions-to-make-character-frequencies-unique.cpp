class Solution {
public:
    int minDeletions(string s) {
        map<char, int> dict_s;
        for(char c : s) {
            dict_s[c]++;
        }

        vector<pair<char, int>> sorted_s(dict_s.begin(), dict_s.end());
        sort(sorted_s.begin(), sorted_s.end(), [](const pair<char, int>& a, const pair<char, int>& b){
            return a.second < b.second;
        });

        set<int> cnt_set;
        int ans = 0;
        for(auto &[char_, cnt] : sorted_s) {
            if(cnt_set.find(cnt) != cnt_set.end()) {
                int sub_cnt = 0;
                while(cnt_set.find(cnt) != cnt_set.end()) {
                    cnt--;
                    sub_cnt++;
                    if(cnt <= 0) {
                        break;
                    }
                }
                ans += sub_cnt;
                if(cnt > 0) {
                    cnt_set.insert(cnt);
                }
            } else {
                cnt_set.insert(cnt);
            }
        }
        return ans;
    }
};