#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int N,M;
int arr[8];
bool visited[8];
vector<int> v;

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

void dfs(int cnt)
{
	if(cnt==M)
	{
		for(int i=0;i<M;i++)
			cout<<arr[i]<<' ';
		cout<<"\n";
		return;
	}
	int before=-1;
	for(int i=0;i<v.size();i++)
	{
		if(!visited[i] && before!=v[i])
		{
			before=v[i];
			visited[i]=true;
			arr[cnt]=v[i];
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