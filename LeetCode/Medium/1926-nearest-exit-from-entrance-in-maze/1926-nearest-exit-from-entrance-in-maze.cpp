class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int dx[4] = {-1,1,0,0};
        int dy[4] = {0,0,-1,1};
        int m = maze.size();
        int n = maze[0].size();
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        queue<pair<int,int>> q;
        q.push({entrance[0], entrance[1]});
        visited[entrance[0]][entrance[1]] = true;
        int ans = 0;

        while(!q.empty()){
            int size = q.size();
            for(int k = 0; k < size; ++k) {
                int x = q.front().first;
                int y = q.front().second;
                q.pop();

                if((x == m-1 || y==n-1 || x==0 || y==0) && (x!=entrance[0]||y!=entrance[1]))
                    return ans;

                for(int i=0; i<4; i++){
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if(nx >= m || ny >= n || nx < 0 || ny < 0 || maze[nx][ny] == '+' || visited[nx][ny])
                        continue;
                    visited[nx][ny] = true;
                    q.push({nx, ny});
                }
            }
            ans++;
        }
        
        return -1;
    }

};