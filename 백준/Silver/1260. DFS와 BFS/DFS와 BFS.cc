#include <bits/stdc++.h>
using namespace std;

#define MAX 1001 //1<=n<=1000
 
vector<int> graph[MAX]; 
bool dfs_visited[MAX];
bool bfs_visited[MAX];
	
void dfs(int x);
void bfs(int y);

int main() {
	int n,m,v;
	cin>>n>>m>>v;
	
	int x,y;
	for(int i=0;i<m;i++){
		cin>>x>>y;
		graph[x].push_back(y);
		graph[y].push_back(x);
	}
	for(int i=1;i<=n;i++){
		sort(graph[i].begin(),graph[i].end());
	}
	dfs(v);
	cout<<'\n';
	bfs(v);
	

	return 0;
}

void dfs(int start){
	dfs_visited[start]=true;
	cout<<start<<' ';
	for(int i=0;i<graph[start].size();i++){
		int y=graph[start][i];
		if(!dfs_visited[y])
			dfs(y);
	}
}

void bfs(int start){
	queue<int> q;
	q.push(start);
	bfs_visited[start]=true;
	while(!q.empty()){
		int x=q.front();
		q.pop();
		cout<<x<<' ';
		for(int i=0;i<graph[x].size();i++){
			int y=graph[x][i];
			if(!bfs_visited[y]){
				q.push(y);
				bfs_visited[y]=true;
			}
		}
	}
}