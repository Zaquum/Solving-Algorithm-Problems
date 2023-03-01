#include <bits/stdc++.h>
using namespace std;
#define MAX 100

int arr[4][8];
int K,sum;
int num[MAX],dir[MAX];
bool visited[4];

void Input(){
	for(int i=0;i<4;i++)
		for(int j=0;j<8;j++)
			scanf("%1d",&arr[i][j]);
	cin>>K;
	for(int i=0;i<K;i++)
		cin>>num[i]>>dir[i];
}


void Rotate(int a,int b){
	int d0=arr[b][0], d1=arr[b][1], d2=arr[b][2], d3=arr[b][3];
	int d4=arr[b][4], d5=arr[b][5], d6=arr[b][6], d7=arr[b][7];
	if(a==1){
		arr[b][0]=d7;
		arr[b][1]=d0;
		arr[b][2]=d1;
		arr[b][3]=d2;
		arr[b][4]=d3;
		arr[b][5]=d4;
		arr[b][6]=d5;
		arr[b][7]=d6;
	}
	else if(a==-1){
		arr[b][0]=d1;
		arr[b][1]=d2;
		arr[b][2]=d3;
		arr[b][3]=d4;
		arr[b][4]=d5;
		arr[b][5]=d6;
		arr[b][6]=d7;
		arr[b][7]=d0;
	}
}

int second(int a){
	if(a==0)
		return 1;
	return 2*second(a-1);
}

void Solution(int x,int y){
	int ny=y*(-1);
	visited[x]=true;
	if(x<3&&!visited[x+1]){
		if(arr[x][2]!=arr[x+1][6])
			Solution(x+1,ny);
	}
	if(x>=1&&!visited[x-1]){
		if(arr[x-1][2]!=arr[x][6])
			Solution(x-1,ny);
	}
	Rotate(y,x);
}

int main() {
	// your code goes here
	Input();
	for(int i=0;i<K;i++){
		memset(visited,false,sizeof(visited));
		Solution(num[i]-1,dir[i]);
	}
	for(int i=0;i<4;i++)
		if(arr[i][0]==1)
			sum+=second(i);
	cout<<sum<<endl;
	return 0;
}