#include <iostream>
using namespace std;

int N,M;
int arr[8]={0,};
bool visited[8]={0,};

void Input()
{
	cin>>N>>M;
}

void dfs(int num, int cnt)
{
	if(cnt==M)
	{
		for(int i=0;i<M;i++)
			cout<<arr[i]<<' ';
		cout<<'\n';
		return;
	}
	for(int i=num;i<N;i++)
	{
		if(!visited[i])
		{
			visited[i]=true;
			arr[cnt]=i+1;
			dfs(i+1, cnt+1);
			visited[i]=false;
		}
	}
}
int main() {
	// your code goes here
	Input();
	dfs(0,0);
	return 0;
}