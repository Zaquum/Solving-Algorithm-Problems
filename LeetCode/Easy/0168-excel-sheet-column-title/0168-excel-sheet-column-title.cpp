class Solution {
public:
    string convertToTitle(int columnNumber) {
        string ans = "";
        while(columnNumber){
            columnNumber--;
            ans = char(int('A') + columnNumber%26) + ans;
            columnNumber = columnNumber/26;
        }
        return ans;
    }
};