#include <bits/stdc++.h>
using namespace std;
#define max 100001

int n,k;
int arr[max];
bool visited[max];
queue<int> q;
int ans;

int bfs(){
	visited[q.front()]=true;
	while(!q.empty()){
		int x=q.front();
		q.pop();
		
		if(x==k)
			return arr[x];
			
		int nx1=x-1;
		int nx2=x+1;
		int nx3=2*x;
			if(0<=nx1&&!visited[nx1]){
				visited[nx1]=true;
				q.push(nx1);
				arr[nx1]=arr[x]+1;
				//cout<<nx1<<arr[nx1]<<endl;
			}
			if(nx2<=100000&&!visited[nx2]){
				visited[nx2]=true;
				q.push(nx2);
				arr[nx2]=arr[x]+1;
				//cout<<nx2<<arr[nx2]<<endl;
			}
			if(nx3<=100000&&!visited[nx3]){
				visited[nx3]=true;
				q.push(nx3);
				arr[nx3]=arr[x]+1;
				//cout<<nx3<<arr[nx3]<<endl;
			}
		}
}

int main() {
	// your code goes here
	cin>>n>>k;
	
	q.push(n);
	
	
	cout<<bfs()<<endl;

	return 0;
}