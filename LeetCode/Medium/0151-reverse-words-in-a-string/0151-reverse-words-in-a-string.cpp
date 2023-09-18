class Solution {
public:
    string reverseWords(string s) {
        int start = 0, end = 0;
        vector<string> result;
        for(int i = 0; i < s.size(); i++){
            if(s[i]!=' ' && (i==0 || s[i-1]==' ')){
                start = i;
            }
            else if(i > 0 && s[i-1] != ' ' && s[i]==' '){
                end = i;
                result.push_back(s.substr(start, end - start));
            }
        }

        if(s[s.size()-1] != ' '){
            result.push_back(s.substr(start, s.size() - start));
        }
        string ans = result[result.size()-1];
        for(int i = result.size() - 2; i >= 0; i--){
            ans += ' ' + result[i];
            // cout << result[i] << " ";
        }
        return ans;
    }
};