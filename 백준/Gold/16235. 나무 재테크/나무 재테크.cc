#include <bits/stdc++.h>
using namespace std;
#define MAX 11

int N,M,K;
int i,j;
int A[MAX][MAX];
int nut[MAX][MAX];
deque<int> tree[MAX][MAX];
vector<int> dead[MAX][MAX];

int dx[]={-1,-1,-1,0,0,1,1,1};
int dy[]={-1,0,1,-1,1,-1,0,1};

void Input(){
	cin>>N>>M>>K;
	for(i=1;i<=N;i++){
		for(j=1;j<=N;j++){
			A[i][j]=5;
			cin>>nut[i][j];
		}
	}
	for(i=0;i<M;i++){
		int x,y,z;
		cin>>x>>y>>z;
		tree[x][y].push_back(z);
	}
}

void spring(){
	for(i=1;i<=N;i++){
		for(j=1;j<=N;j++){
			int size = tree[i][j].size();
			while(size--){
				int age=tree[i][j].front();
				tree[i][j].pop_front();
				if(A[i][j]<age){
					dead[i][j].push_back(age);
					continue;
				}
				A[i][j]-=age;
				tree[i][j].push_back(age+1);
			}
		}
	}
}

void summer(){
	for(i=1;i<=N;i++){
		for(j=1;j<=N;j++){
			int size=dead[i][j].size();
			while(size--){
				int nutrient = dead[i][j].back();
				dead[i][j].pop_back();
				A[i][j]+=(nutrient/2);
			}
		}
	}
}
void fall(){
	for(i=1;i<=N;i++){
		for(j=1;j<=N;j++){
			for(int k=0;k<tree[i][j].size();k++){
				int age=tree[i][j][k];
				if(age%5 == 0){
					for(int dir=0;dir<8;dir++){
						int ni=i+dx[dir];
						int nj=j+dy[dir];
						if(ni<1||ni>N||nj<1||nj>N)
							continue;
						tree[ni][nj].push_front(1);
					}
				}
			}
		}
	}
}
void winter(){
	for(i=1;i<=N;i++){
		for(j=1;j<=N;j++){
			A[i][j]+=nut[i][j];
		}
	}
}

void Solution(){
	while(K--){
		spring();
		summer();
		fall();
		winter();
	}
	int cnt=0;
	for(i=1;i<=N;i++){
		for(j=1;j<=N;j++){
			cnt+=tree[i][j].size();
		}
	}
	cout<<cnt<<endl;
}
int main() {
	// your code goes here
	Input();
	Solution();
	return 0;
}