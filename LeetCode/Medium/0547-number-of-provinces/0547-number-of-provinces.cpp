class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<bool> visited(n, false);
        int cnt = 0;
        for(int i=0; i<n; i++){
            if(!visited[i]){
                dfs(isConnected, visited, i);
                cnt++;
            }
        }
        return cnt;
    }

    void dfs(vector<vector<int>>& map, vector<bool> &visited, int n){
        visited[n] = true;
        for (int i=0; i< map[n].size(); i++){
            if(i==n || visited[i] || map[n][i]==0)
                continue;
            dfs(map, visited, i);
        }
    }
};