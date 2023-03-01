#include <bits/stdc++.h>
using namespace std;
#define MAX 100

int N,K,L;
int MAP[MAX][MAX];

int dx[]={-1,1,0,0};
int dy[]={0,0,-1,1};

vector<pair<int,char>> V;


void input()
{
	cin>>N>>K;
	int x,y;
	for(int i=0;i<K;i++)
	{
		cin>>x>>y;
		MAP[x-1][y-1]=1;
	}
	cin>>L;
	for(int i=0;i<L;i++)
	{
		int a;
		char b;
		cin>>a>>b;
		V.push_back(make_pair(a,b));
	}
}
int Turn_Dir(int a, char b)
{
	if(b=='L')
	{
		if(a==0)
			return 2;
		else if(a==1)
			return 3;
		else if(a==2)
			return 1;
		else if(a==3)
			return 0;
	}
	else if(b=='D')
	{
		if(a==0)
			return 3;
		else if(a==1)
			return 2;
		else if(a==2)
			return 0;
		else if(a==3)
			return 1;
	}
}

void Solution()
{
	deque<pair<int,int>> q;
	int x=0;
	int y=0;
	int d=3;
	int Time=0;
	int Idx=0;
	q.push_back(make_pair(x,y));
	MAP[x][y]=2;
	
	while(1)
	{
		Time++;
		
		int nx=x+dx[d];
		int ny=y+dy[d];
		
		if((nx<0||ny<0||nx>=N||ny>=N)||MAP[nx][ny]==2)
		{
			break;
		}
		else if(MAP[nx][ny]==0)
		{
			MAP[nx][ny]=2;
			MAP[q.back().first][q.back().second]=0;
			q.pop_back();
			q.push_front(make_pair(nx,ny));
		}
		else if(MAP[nx][ny]==1)
		{
			MAP[nx][ny]==2;
			q.push_front(make_pair(nx,ny));
		}
		if(Idx<V.size())
		{
			if(Time==V[Idx].first)
			{
				if(V[Idx].second=='L')
					d=Turn_Dir(d,'L');
				else if(V[Idx].second='D')
					d=Turn_Dir(d,'D');
				Idx++;
			}
		}
		x=nx;
		y=ny;
	}
	cout<<Time<<endl;
}

int main(){
	input();
	Solution();
}