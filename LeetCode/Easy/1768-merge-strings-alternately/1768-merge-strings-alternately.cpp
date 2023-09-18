class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n1 = word1.size(), n2 = word2.size();
        int i=0, j=0;
        string ans = "";
        while (i<n1 && j<n2){
            if(i == j){
                ans += word1[i];
                i++;
            }
            else if(i>j){
                ans += word2[j];
                j++;
            }
        }
        if (i != n1){
            ans += word1.substr(i, n1 - i + 1); // 012345
        }
        else
            ans += word2.substr(j, n2 - j + 1);
        return ans;
    }
};