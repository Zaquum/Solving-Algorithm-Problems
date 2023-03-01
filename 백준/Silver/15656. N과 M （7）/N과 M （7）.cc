#include <iostream>
#include <algorithm>
using namespace std;

int arr[8],arr2[8];
int N,M;

void Input()
{
	cin>>N>>M;
	for(int i=0;i<N;i++)
		cin>>arr2[i];
	sort(arr2,arr2+N);
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
		arr[cnt]=arr2[i];
		dfs(cnt+1);
	}
}

int main() {
	// your code goes here
	Input();
	dfs(0);
	return 0;
}