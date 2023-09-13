class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& image) {
        int n = image.size();
        vector<vector<int>> ans (n, (vector<int> (n,0)));
        for(int i=0; i<image.size(); i++){
            for(int j=0; j<image[0].size(); j++){
                ans[i][n-j-1] = 1 - image[i][j];
            }
        }
        return ans;
    }
};