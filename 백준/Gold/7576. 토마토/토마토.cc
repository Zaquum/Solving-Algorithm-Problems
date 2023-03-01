#include <bits/stdc++.h>
using namespace std;
#define MAX 1000

int n,m;
int arr[MAX][MAX];
bool visited[MAX][MAX];
int cnt[MAX][MAX]={0,};
int dx[]={-1,1,0,0};
int dy[]={0,0,-1,1};
queue<pair<int,int>> q;

int get_max(int a, int b){
	return a>b?a:b;
}

void bfs(void){
	visited[q.front().first][q.front().second]=true;
	while(!q.empty()){
		int xx=q.front().first;
		int yy=q.front().second;
		q.pop();
		for(int i=0;i<4;i++){
			int nx=xx+dx[i];
			int ny=yy+dy[i];
			if(0<=nx&&nx<n&&0<=ny&&ny<m){
				if(arr[nx][ny]==0&&!visited[nx][ny]){
					q.push(make_pair(nx,ny));
					visited[nx][ny]=true;
					cnt[nx][ny]=cnt[xx][yy]+1;
				}	
			}
		}
	}
}
int main() {
	// your code goes here
	cin>>m>>n;
	int max=0;
	
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			cin>>arr[i][j];
			if(arr[i][j]==1)
				q.push(make_pair(i,j));
		}
	}
	
	bfs();

	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			max=get_max(max,cnt[i][j]);
		}
	}
	
	//다 익지 못한 경우
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(arr[i][j]==0&&!visited[i][j]){
				cout<<"-1"<<endl;
				return 0;
			}
		}
	}
	
	cout<<max<<endl;
	return 0;
}