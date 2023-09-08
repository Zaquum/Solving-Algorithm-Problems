class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result;
        // result.push_back({1});
        // for(int i=0; i<numRows-1;i++){
        //     vector<int> newRow;
        //     newRow.push_back(1);
        //     for(int j=0; j<i; j++){
        //         int elem = result[i][j] + result[i][j+1];
        //         newRow.push_back(elem);
        //     }
        //     newRow.push_back(1);
        //     result.push_back(newRow);
        // }
        // return result;
        for(int i=0; i<numRows; i++){
            vector<int> newRow(i+1, 1);
            for(int j=1; j<i; j++){
                newRow[j] = result[i-1][j-1] + result[i-1][j];
            }
            result.push_back(newRow);
        }
        return result;
    }
};