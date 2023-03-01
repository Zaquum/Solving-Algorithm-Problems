#include <iostream>
using namespace std;

int arr[7];
int visited[7];
int N,M;

void Input()
{
	cin>>N>>M;
}

void dfs(int cnt)
{
	if(cnt==M)
	{
		for(int i=0;i<M;i++)
			cout<<arr[i]<<' ';
		cout<<'\n';
		return;
	}
	
	for(int i=0;i<N;i++)
	{
		if(visited[i]<M)
		{
			visited[i]=visited[i]+1;
			arr[cnt]=i+1;
			dfs(cnt+1);
			visited[i]=visited[i]-1;
		}
	}
}

int main() {
	// your code goes here
	Input();
	dfs(0);
	return 0;
}