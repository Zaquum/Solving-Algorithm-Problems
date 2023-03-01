#include <bits/stdc++.h>
using namespace std;
#define MAX 25

int aprt[MAX][MAX];
vector<int> ans;
bool visited[MAX][MAX];
int n;
int dx[]={-1,1,0,0};
int dy[]={0,0,-1,1};
int cnt;

void dfs(int x, int y){
	visited[x][y]=true;
	cnt++;
	for(int i=0;i<4;i++){
		int newX=x+dx[i];
		int newY=y+dy[i];
		if(0<=newX&&newX<n&&0<=newY&&newY<n)
		 if(aprt[newX][newY]==1&&!visited[newX][newY])
			dfs(newX,newY);
	}
}

/*
void bfs(int start){
	queue<int> q;
	q.push(start);
	visited[start]=true;
	cnt++;
	while(!q.empty()){
	int x=q.front();
	q.pop();
	for(int i=0;i<network[x].size();i++){
		int next=network[x][i];
		if(!visited[y]){
			q.push(y);
			visited[y]=true;
			cnt++;
		}
	}
	}
}
*/
int main() {
	// your code goes here
	cin>>n;
	
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
			scanf("%1d",&aprt[i][j]);
		
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			if(aprt[i][j]==1&&!visited[i][j]){
				cnt=0;
				dfs(i,j);
				ans.push_back(cnt);
			}
		}
	}
	
	sort(ans.begin(),ans.end());
	cout<<ans.size()<<endl;
	for(int i=0;i<ans.size();i++)
		cout<<ans[i]<<endl;
	return 0;
}