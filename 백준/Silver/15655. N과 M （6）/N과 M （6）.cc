#include <iostream>
#include <algorithm>
using namespace std;

int arr[8];
int arr2[8];
bool visited[8];
int N,M;

void Input()
{
	cin>>N>>M;
	for(int i=0;i<N;i++)
		cin>>arr2[i];
	sort(arr2,arr2+N);
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
			arr[cnt]=arr2[i];
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