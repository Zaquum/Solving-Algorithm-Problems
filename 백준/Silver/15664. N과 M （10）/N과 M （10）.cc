#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N,M;
int arr[8];
vector<int> v;
bool visited[8];

void Input()
{
	int a;
	cin>>N>>M;
	for(int i=0;i<N;i++)
	{
		cin>>a;
		v.push_back(a);
	}
	sort(v.begin(),v.end());
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
	
	int before=-1;
	for(int i=num;i<N;i++)
	{
		if(before!=v[i])
		{
			before = v[i];
			arr[cnt]=v[i];
			dfs(i+1, cnt+1);
		}	
	}
}
int main() {
	// your code goes here
	Input();
	dfs(0,0);
	return 0;
}