#include <bits/stdc++.h>
using namespace std;
#define max 50

int arr[max][max];
bool visited[max][max];
vector<int> ans;
vector<int> ans2;
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
int m, n, k;
int cnt = 0;

void dfs(int x, int y) {
	visited[x][y] = true;
	cnt++;
	for (int i = 0; i < 4; i++)
	{
		int nx = x + dx[i];
		int ny = y + dy[i];
		if (0 <= nx && nx < m && 0 <= ny && ny < n)
			if (arr[nx][ny] == 1 && !visited[nx][ny])
				dfs(nx, ny);
	}
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> m >> n >> k;

		memset(arr, 0, sizeof(arr));
		memset(visited, false, sizeof(visited));
		ans.clear();

		for (int j = 0; j < k; j++) {
			int x, y;
			cin >> x >> y;
			arr[x][y] = 1;
		}
		//int ans = 0;
		for (int xx = 0; xx < m; xx++) {
			for (int yy = 0; yy < n; yy++) {
				if (arr[xx][yy] == 1 && !visited[xx][yy]) {
					cnt = 0;
					//ans++;
					dfs(xx, yy);
					ans.push_back(cnt);
				}
			}
		}
		ans2.push_back(ans.size());
	}
	for (int i = 0; i < t; i++)
		cout << ans2[i] << endl;
	return 0;
}