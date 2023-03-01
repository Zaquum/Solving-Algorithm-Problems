#include <iostream>
using namespace std;

int arr[8]={0,};
bool visited[8]={0,};
int N,M;

void Input(){
	cin>>N>>M;
}

void dfs(int cnt)
{
	for(int i=0;i<N;i++)
	{
		if(cnt==M)
		{
			for(int i=0;i<M;i++)
				cout<<arr[i]<<' ';
			cout<<'\n';
			return;
		}
		
		if(!visited[i])
		{
			visited[i]=true;
			arr[cnt]=i+1;
			dfs(cnt+1);
			visited[i]=false;
		}
	}
}
int main() {
	// your code goes here
	Input();
	dfs(0);
	return 0;
}