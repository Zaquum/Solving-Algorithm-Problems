#include <bits/stdc++.h>
using namespace std;

int R,C,T;
int A[50][50];
int B[50][50];
int i,j;
vector<pair<int,int>> Condition;
int dx[]={-1,1,0,0};
int dy[]={0,0,-1,1};

void Input(){
	cin>>R>>C>>T;
	for(i=0;i<R;i++){
		for(j=0;j<C;j++){
			cin>>A[i][j];
			if(A[i][j]==-1)
				Condition.push_back({i,j});
		}
	}
}
bool boundary(int x, int y){
	if(x>=0&&x<R&&y>=0&&y<C)
		return true;
	else
		return false;
}

void Spread(){
	memset(B,0,sizeof(B));
	for(i=0;i<R;i++){
		for(j=0;j<C;j++){
			if(A[i][j]>0){
				int spread=A[i][j]/5;
				int cnt=0;
				if(spread>0){
					for(int k=0;k<4;k++){
						int nx=i+dx[k];
						int ny=j+dy[k];
						if(!boundary(nx,ny)||A[nx][ny]==-1){
							continue;
						}
						cnt++;
						B[nx][ny]+=spread;
					}
					B[i][j]=B[i][j]-cnt*spread;
				}
			}
		}
	}
	for(i=0;i<R;i++)
		for(j=0;j<C;j++)
			A[i][j]+=B[i][j];
}

void Clean(){
	int x0=Condition[0].first;
	int y0=Condition[0].second;
	int x1=Condition[1].first;
	int y1=Condition[1].second;
	int tmp1,tmp2;
	
	for(i=C-1;i>y0+1;i--){
		if(i==C-1)
			tmp1=A[x0][C-1];
		A[x0][i]=A[x0][i-1];
	}
	A[x0][y0+1]=0;
	for(i=0;i<x0;i++){
		if(i==0){
			tmp2=A[0][C-1];
			A[i][C-1]=A[i+1][C-1];
		}
		else if(i==x0-1)
			A[i][C-1]=tmp1;
		else
			A[i][C-1]=A[i+1][C-1];
	}
	for(i=0;i<C-1;i++){
		if(i==0){
			tmp1=A[0][i];
			A[0][i]=A[0][i+1];
		}
		else if(i==C-2)
			A[0][i]=tmp2;
		else
			A[0][i]=A[0][i+1];
	}
	for(i=x0-1;i>0;i--){
		if(i==1)
			A[i][0]=tmp1;
		else
			A[i][0]=A[i-1][0];
	}
	
		
	for(i=C-1;i>y1+1;i--){
		if(i==C-1)
			tmp1=A[x1][C-1];
		A[x1][i]=A[x1][i-1];
	}
	A[x1][y1+1]=0;
	for(i=R-1;i>x1;i--){
		if(i==x1+1)
			A[i][C-1]=tmp1;
		else if(i==R-1){
			tmp2=A[i][C-1];
			A[i][C-1]=A[i-1][C-1];
		}
		else
			A[i][C-1]=A[i-1][C-1];
	}
	for(i=0;i<C-1;i++){
		if(i==0){
			tmp1=A[R-1][i];
			A[R-1][i]=A[R-1][i+1];
		}
		else if(i==C-2)
			A[R-1][i]=tmp2;
		else
			A[R-1][i]=A[R-1][i+1];
	}
	for(i=x1+1;i<R-1;i++){
		if(i==R-2)
			A[i][0]=tmp1;
		else
			A[i][0]=A[i+1][0];
	}
}

void Solution(){
	while(T--){
		Spread();
		Clean();
	}
	int sum=0;
	for(i=0;i<R;i++){
		for(j=0;j<C;j++){
//			cout<<A[i][j]<<" ";
			if(A[i][j]>0)
				sum+=A[i][j];
		}
//		cout<<endl;
	}
	cout<<sum<<endl;
}

int main() {
	// your code goes here
	Input();
	Solution();
	return 0;
}