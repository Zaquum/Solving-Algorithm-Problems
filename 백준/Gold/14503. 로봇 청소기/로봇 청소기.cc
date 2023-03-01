#include <bits/stdc++.h>
using namespace std;
#define MAX 50

int N,M;
int sx,sy,d;
int cnt=0;
int MAP[MAX][MAX];

int dx[]={-1,0,1,0};
int dy[]={0,1,0,-1};

void input(){
	cin>>N>>M;
	cin>>sx>>sy>>d;
	for(int i=0;i<N;i++)
		for(int j=0;j<M;j++)
			cin>>MAP[i][j];
			
}


int Rotate(int dir){
	if(dir==0) return 3;
	else if(dir==1) return 0;
	else if(dir==2) return 1;
	else if(dir==3) return 2;
}

void bfs(){
	MAP[sx][sy]=2;
	cnt++;
	int x=sx;
	int y=sy;
	
	int nx,ny,nd;

	while(1){
		int tmp_d=d;
		int Cannot_clean=0;
		bool Can_clean=false;
		
		for(int i=0;i<4;i++){
			nd=Rotate(d);
			nx=x+dx[nd];
			ny=y+dy[nd];
			if(MAP[nx][ny]==0){
				Can_clean = true;
				break;
			}
			else if((nx<0||nx>=N||ny<0||ny>=M)||MAP[nx][ny]==1||MAP[nx][ny]==2){
				Cannot_clean++;
				d=nd;
			}
		}
		if(Can_clean){
			d=nd;
			MAP[nx][ny]=2;
			cnt++;
//			cout<<nx<<" "<<ny<<endl;
		}
		if(Cannot_clean==4){
			nx=x-dx[tmp_d];
			ny=y-dy[tmp_d];
			d=tmp_d;
//			cout<<nx<<" "<<ny<<endl;
			if((nx<0||ny<0||nx>=N||ny>=M)||MAP[nx][ny]==1)
				break;
		}
		x=nx;
		y=ny;
	}
	cout<<cnt<<endl;
}

int main() {
	// your code goes here
	input();
	bfs();
	return 0;
}