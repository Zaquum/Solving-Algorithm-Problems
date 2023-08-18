class Solution {
public:
    int maximalNetworkRank(int n, vector<vector<int>>& roads) {
        vector<int> degrees(n,0);
        vector<vector<bool>> connected(n, vector<bool>(n, false));

        for(int i=0; i<roads.size(); i++){
            degrees[roads[i][0]]++;
            degrees[roads[i][1]]++;
            connected[roads[i][0]][roads[i][1]] = true;
            connected[roads[i][1]][roads[i][0]] = true;
        }
        int max_rank = 0;
        for(int i=0; i<n;i++){
            for(int j=i+1; j<n; j++){
                int rank = degrees[i] + degrees[j];
                if(connected[i][j])
                    rank -= 1;
                max_rank = std::max(max_rank, rank);
            }
        }
        return max_rank;
    }
};