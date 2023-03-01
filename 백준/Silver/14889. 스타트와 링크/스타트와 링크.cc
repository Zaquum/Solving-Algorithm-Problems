#include <bits/stdc++.h>
using namespace std;
#define MAX 21

int arr[MAX][MAX];
int N;
bool check[21];
int ans=1000000000;

void Input(){
	cin>>N;
	for(int i=1;i<=N;i++)
		for(int j=1;j<=N;j++)
			cin>>arr[i][j];
}

void dfs(int x, int idx){
	if(x==N/2){
		int start,link;
		start=0;
		link=0;
		for(int i=1;i<=N;i++){
			for(int j=1;j<=N;j++){
				if(check[i]&&check[j])
					start+=arr[i][j];
				if(!check[i]&&!check[j])
					link+=arr[i][j];
			}
		}
		int tmp=abs(start-link);
		if(ans>tmp)
			ans=tmp;
		return;
	}
	for(int i=idx;i<N;i++){
		check[i]=true;
		dfs(x+1,i+1);
		check[i]=false;
	}
}

int main() {
	// your code goes here
	Input();
	dfs(0,1);
	cout<<ans<<endl;
	return 0;
}