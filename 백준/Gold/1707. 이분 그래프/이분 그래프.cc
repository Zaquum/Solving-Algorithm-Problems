#include <bits/stdc++.h>
using namespace std;
#define MAX 20001
#define RED 1
#define BLUE 2

int k,v,e;
vector<int> point[MAX];
int visited[MAX];

void dfs(int start){
	if(!visited[start])
		visited[start]=RED;

	for(int i=0;i<point[start].size();i++){
		int next=point[start][i];
		if(!visited[next]){
			if(visited[start]==RED)
				visited[next]=BLUE;
			else if(visited[start]==BLUE)
				visited[next]=RED;
			dfs(next);
		}
	}
}

void isBipGraph(){
	for(int i=0;i<v;i++)
	{
		for(int j=0;j<point[i].size();j++)
		{
			int next=point[i][j];
			if(visited[i]==visited[next])
			{
				cout<<"NO"<<endl;
				return;
			}
		}
	}
	cout<<"YES"<<endl;
	return;
}

int main() {
	// your code goes here
	cin>>k;
	
	int x,y,cnt2;
	for(int i=0;i<k;i++){
		cin>>v>>e;
		for(int l=0;l<e;l++){
			cin>>x>>y;
			point[x].push_back(y);
			point[y].push_back(x);
		}
		for(int j=1;j<=v;j++){
			if(!visited[j])
				dfs(j);
		}
		isBipGraph();	
		for(int j=0;j<=v;j++)
			point[j].clear();
		memset(visited,false,sizeof(visited));
	}
	return 0;
}
