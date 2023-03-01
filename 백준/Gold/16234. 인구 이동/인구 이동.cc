#include <bits/stdc++.h>
using namespace std;

int N,L,R;
int arr[50][50];
bool visited[50][50];
int dx[]={-1,1,0,0};
int dy[]={0,0,-1,1};
vector<pair<int,int>> v;
int people,num;

void Input(){
	cin>>N>>L>>R;	
	for(int i=0;i<N;i++)
		for(int j=0;j<N;j++)
			cin>>arr[i][j];
}

void DFS(int x,int y){
	for(int i=0;i<4;i++){
		int nx=x+dx[i];
		int ny=y+dy[i];
		int k=abs(arr[x][y]-arr[nx][ny]);
		if(nx<0||nx>=N||ny<0||ny>=N)
			continue;
		if(!visited[nx][ny]&&k>=L&&k<=R){
			visited[nx][ny]=true;
			v.push_back({nx,ny});
			people+=arr[nx][ny];
			num++;
			DFS(nx,ny);
		}
	}
}

void Solve(){
	int result=0;
	while(1){
		memset(visited,false,sizeof(visited));
		
		bool found = false;
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				if(visited[i][j])
					continue;
					
				visited[i][j]=true;
				people=arr[i][j];
				num=1;
				
				v.clear();
				v.push_back({i,j});
				DFS(i,j);
				
				if(num>=2){
					found=true;
					for(int k=0;k<v.size();k++)
						arr[v[k].first][v[k].second]=people/num;
				}
			}
		}
		if(found){
			result++;
		}
		else
			break;
	}
	cout<<result<<endl;
}

int main() {
	// your code goes here
	Input();
	Solve();
	return 0;
}