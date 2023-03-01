#include <iostream>
#define MAX 100

using namespace std;

int N, maxx;
int map[MAX][MAX];
bool water[MAX][MAX];
int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};

void input()
{
    int x;
    cin>>N;
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
            {
                cin >> x;
                if(x>=maxx)
                    maxx = x;
                map[i][j] = x;
            }
    }
}

void rain(int n)
{
    for(int i=0;i<N;i++) // 초기화
    {
        for(int j=0;j<N;j++)
            {
                water[i][j] = false;
            }
    }

    for(int i=0;i<N;i++) // 잠긴 칸 = true
    {
        for(int j=0;j<N;j++)
            {
                if(map[i][j]<=n)
                {
                    water[i][j] = true;
                }
            }
    }
}

void DFS(int x, int y)
{
    water[x][y] = true;

    for(int i=0;i<4;i++)
    {
        int new_x = x + dx[i];
        int new_y = y + dy[i];
        if(new_x < 0 || new_x >= N)
            continue;
        if(new_y < 0 || new_y >= N)
            continue;
        if(!water[new_x][new_y])
            DFS(new_x,new_y);
    }
}

int travel(int n)
{
    int cnt = 0;
    rain(n); // 물에 잠겨 -> true

    for(int i=0;i<N;i++) // DFS
    {
        for(int j=0;j<N;j++)
            {
                if(!water[i][j])
                {
                    DFS(i,j);
                    cnt++;
                }
            }
    }
    return cnt;
}


int main()
{
    int max_cnt = 0;
    input();
    for(int i = 0; i<=maxx; i++)
    {
        int now_cnt = travel(i);
        if(max_cnt<=now_cnt)
            max_cnt = now_cnt;

    }
    cout << max_cnt << endl;
    return 0;
}