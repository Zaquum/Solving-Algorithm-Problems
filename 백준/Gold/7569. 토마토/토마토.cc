#include <bits/stdc++.h>
using namespace std;
#define MAX 100
 
int n,m,h;
int arr[MAX][MAX][MAX];
bool visited[MAX][MAX][MAX];
int cnt[MAX][MAX][MAX]={0,};
int dx[]={-1,1,0,0,0,0};
int dy[]={0,0,-1,1,0,0};
int dz[]={0,0,0,0,-1,1};
queue<pair<pair<int,int>,int>> q;
 
int get_max(int a, int b){
	return a>b?a:b;
}
 
void bfs(void){
	visited[q.front().first.first][q.front().first.second][q.front().second]=true;
	while(!q.empty()){
		int xx=q.front().first.first;
		int yy=q.front().first.second;
		int zz=q.front().second;
		q.pop();
		for(int i=0;i<6;i++){
			int nx=xx+dx[i];
			int ny=yy+dy[i];
			int nz=zz+dz[i];
			if(0<=nx&&nx<n&&0<=ny&&ny<m&&0<=nz&&nz<h){
				if(arr[nx][ny][nz]==0&&!visited[nx][ny][nz]){
					q.push(make_pair(make_pair(nx,ny),nz));
					visited[nx][ny][nz]=true;
					cnt[nx][ny][nz]=cnt[xx][yy][zz]+1;
				}	
			}
		}
	}
}
int main() {
	// your code goes here
	cin>>m>>n>>h;
	int max=0;
	
	for(int k=0;k<h;k++){
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				cin>>arr[i][j][k];
				if(arr[i][j][k]==1)
					q.push(make_pair(make_pair(i,j),k));
			}
		}
	}
 
	bfs();

 
	//다 익지 못한 경우
	for(int k=0;k<h;k++){
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if(arr[i][j][k]==0&&!visited[i][j][k]){
					cout<<"-1"<<endl;
					return 0;
				}
				else if(max<cnt[i][j][k])
					max = cnt[i][j][k];
			}
		}
	}
	/*
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			max=get_max(max,cnt[i][j]);
		}
	}
	*/
 
	cout<<max<<endl;
	return 0;
}