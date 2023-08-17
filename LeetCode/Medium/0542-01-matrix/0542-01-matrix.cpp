class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        queue<pair<int,int>> q;
        int dy[4] = {1,-1,0,0};
        int dx[4] = {0,0,1,-1};
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(mat[i][j]==0)
                    q.push({i,j});
                else
                    mat[i][j] = m*n;
            }
        }
        while(!q.empty()){
            int y = q.front().first;
            int x = q.front().second;
            q.pop();
            for(int i=0; i<4; i++){
                int ny = y+dy[i];
                int nx = x+dx[i];
                if(0>ny || ny >= m)
                    continue;
                if(0>nx || nx >= n)
                    continue;
                if(mat[ny][nx]>mat[y][x]+1){
                    q.push({ny,nx});
                    mat[ny][nx] = mat[y][x]+1;
                }
            }
        }
        return mat;
    }
};