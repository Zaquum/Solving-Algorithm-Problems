class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result;
        result.push_back({1});
        for(int i=0; i<numRows-1;i++){
            vector<int> newRow;
            newRow.push_back(1);
            for(int j=0; j<i; j++){
                int elem = result[i][j] + result[i][j+1];
                newRow.push_back(elem);
            }
            newRow.push_back(1);
            result.push_back(newRow);
        }
        return result;
    }
};