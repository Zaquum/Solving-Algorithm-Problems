#include <bits/stdc++.h>
using namespace std;
#define max 100

int n, m;
int arr[max][max];
bool visited[max][max];
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
int cnt[max][max] = { 0, };

/*
void dfs(int x, int y){
	visited[x][y]=true;
	cnt++;
	for(int i=0;i<4;i++){
		int nx=x+dx[i];
		int ny=y+dy[y];
		if(0<=nx&&nx<n&&0<=ny&&ny<m)
			if(arr[nx][ny]&!visited[nx][ny])
				dfs(nx,ny);
	}
}
*/

void bfs(int x, int y) {
	visited[x][y] = true;
	queue<pair<int, int>> q;
	q.push(make_pair(x, y));
	cnt[x][y]++;

	while (!q.empty()) {
		int xx = q.front().first;
		int yy = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nx = xx + dx[i];
			int ny = yy + dy[i];
			if (0 <= nx && nx < n && 0 <= ny && ny < m) {
				if (arr[nx][ny]==1 && !visited[nx][ny]) {
					q.push(make_pair(nx, ny));
					visited[nx][ny] = true;
					cnt[nx][ny] = cnt[xx][yy] + 1;
				}
			}
		}
	}

}

int main(void) {
	cin >> n >> m;

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			scanf("%1d", &arr[i][j]);
		}
	}

	bfs(0, 0);
	cout << cnt[n-1][m-1] << endl;

	return 0;
}