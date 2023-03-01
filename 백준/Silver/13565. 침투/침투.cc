#include <iostream>
#include <vector>
//#include <cstring>
#define MAX 1000

using namespace std;

int map[MAX][MAX];
bool visited[MAX][MAX];
int N,M;
int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};
bool finish = false;
string s;

void DFS(int x, int y)
{
    visited[x][y] = true;   
    for(int i=0; i<4; i++)
    {
        int new_x = x + dx[i];
        int new_y = y + dy[i];
        if(new_x >= M || new_x < 0)
            continue;
        if(new_y >= N || new_y < 0)
            continue;
        if(new_x == M-1)
        {
            finish = true;
            return ;
        }
        if(map[new_x][new_y]==0 && !visited[new_x][new_y])    
            DFS(new_x, new_y);
    }
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> M >> N;
    for(int i=0; i<M; i++)
    {
        cin >> s;
        for(int j=0; j<N; j++)
            // scanf("%1d", &map[i][j]);
            map[i][j] = s[j] - '0';
    }
    for(int i=0; i<N; i++)
    {
        if(map[0][i]==0)
        {
            // memset(visited, false, sizeof(visited));
            DFS(0, i);
            if(finish)
            {
                cout << "YES" << endl;
                return 0;
            }
        }
    }

    cout << "NO" << endl;
    return 0;
}