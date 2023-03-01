#include <bits/stdc++.h>
using namespace std;
#define max 300

int l,testcase;
int arr[max][max];
int cnt[max][max];
bool visited[max][max];
int dx[]={-2,-2,2,2,-1,-1,1,1};
int dy[]={-1,1,-1,1,-2,2,-2,2};
int x_1,x_2,y_1,y_2;

void bfs(){
	memset(cnt,0,sizeof(cnt));
	memset(visited,false,sizeof(visited));
	
	queue<pair<int,int>> q;
	q.push(make_pair(x_1,y_1));
	visited[x_1][y_1]=true;
	while(!q.empty()){
		int xx=q.front().first;
		int yy=q.front().second;
		if(xx==x_2&&yy==y_2){
			cout<<cnt[xx][yy]<<endl;
			break;
		}
		q.pop();
		for(int i=0;i<8;i++){
			int nx=xx+dx[i];
			int ny=yy+dy[i];
			if(nx<0||nx>=l||ny<0||ny>=l)
				continue;
			if(visited[nx][ny])
				continue;
			q.push(make_pair(nx,ny));
			visited[nx][ny]=true;
			cnt[nx][ny]=cnt[xx][yy]+1;
		}
	}
}

int main(){
	cin>>testcase;
	for(int i=0;i<testcase;i++){
	cin>>l;
	cin>>x_1>>y_1;
	cin>>x_2>>y_2;
	bfs();
	}
	
	return 0;
}