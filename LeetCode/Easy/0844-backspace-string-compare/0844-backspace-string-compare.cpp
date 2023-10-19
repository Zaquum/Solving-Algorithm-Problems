class Solution {
public:
    bool backspaceCompare(string s, string t) {
        string s_;
        string t_;

        for(auto &str : s){
            if(str == '#') {
                if(!s_.empty()) {
                    s_.pop_back();
                }
            } else {
                s_.push_back(str);
            }
        }

        for(auto &str : t){
            if(str == '#') {
                if(!t_.empty()) {
                    t_.pop_back();
                }
            } else {
                t_.push_back(str);
            }
        }

        return s_ == t_;
    }
};