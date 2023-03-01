#include <iostream>
using namespace std;

int arr[7];
bool visited[7];
int N,M;

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
//			visited[i]=true;
			arr[cnt]=i+1;
			dfs(i,cnt+1);
//			visited[i]=false;
	}
}

int main() {
	// your code goes here
	Input();
	dfs(0,0);
	return 0;
}