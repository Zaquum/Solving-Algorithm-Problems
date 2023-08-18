int maximalNetworkRank(int n, int** roads, int roadsSize, int* roadsColSize){
        // vector<int> degrees(n,0);
        // vector<vector<bool>> connected(n, vector<bool>(n, false));
        int degrees[100] = {0};
        bool connected[100][100] = {false};

        for(int i=0; i<roadsSize; i++){
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
                if(rank > max_rank)
                    max_rank = rank;
            }
        }
        return max_rank;
}