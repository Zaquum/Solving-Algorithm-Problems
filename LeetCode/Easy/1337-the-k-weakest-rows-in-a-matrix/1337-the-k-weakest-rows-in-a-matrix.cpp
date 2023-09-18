class Solution {
public:
    struct cmp {
        bool operator()(pair<int, int> a, pair<int, int> b){
            if (a.second == b.second)
                return a.first > b.first;
            return a.second > b.second;
            
        }
    };

    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        int m = mat.size(), n = mat[0].size();
        priority_queue<pair<int, int>, vector<pair<int, int>>, cmp> q;

        for(int i = 0; i < m; i++) {
            int soldiers = 0;
            for(int j = 0; j < n; j++) {
                if (mat[i][j] == 1) {
                    soldiers++;
                } else {
                    break;
                }
            }
            q.push({i, soldiers});
        }

        vector<int> result;
        for (int i = 0; i < k; i++) {
            result.push_back(q.top().first);
            q.pop();
        }
        return result;
        // for(int i = 0; i < row.size(); i++){
        //     while(i && row[i].second <= row[i-1].second){
        //         pair<int,int> tmp = row[i];
        //         row[i] = row[i-1]; 
        //         row[i-1] = tmp;
        //         i--;
        //     }
        // }
        // vector<int> result;

        // for(int i=0; i<row.size();i++){
        //     result.push_back(row[i].first);
        // }
        // return result;
    }
};