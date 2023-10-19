class Solution {
public:
    bool backspaceCompare(string s, string t) {
        string s_;
        string t_;

        for(auto &str : s){
            if(str == '#'){
                s_.pop_back();
                continue;
            }
            s_.push_back(str);
        }

        for(auto &str : t){
            if(str == '#'){
                t_.pop_back();
                continue;
            }
            t_.push_back(str);
        }
        return s_ == t_;
    }
};