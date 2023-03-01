#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

#define MAX 101

using namespace std;

int N, M;

// vector<pair<int,int>> snake;
// vector<pair<int,int>> ladder;
int map[MAX] = {0};
bool visited[MAX] = {false};

// DFS 실패
// int DFS(int a, int count)
// {
//     if(a >= 100)
//     {
//         return count++;
//     }
//     for(int i=0;i<snake.size();i++)
//     {
//         if(a == snake[i].first)
//             DFS(snake[i].second, count++);
//     }
//     for(int i=0;i<ladder.size();i++)
//     {
//         if(a == ladder[i].first)
//             DFS(ladder[i].second, count++);
//     }
//     cnt += min({DFS(a+1, count++),DFS(a+2, count++),DFS(a+3, count++),DFS(a+4, count++),DFS(a+5, count++),DFS(a+6, count++)});
//     return count;
// }

void solve()
{
    // DFS 실패
    // cnt=0;
    // DFS(1,0); 
    // cout << cnt << endl;
    queue<pair<int,int>> que;
    que.push({1,0});
    while(!que.empty())
    {
        int now = que.front().first;
        int count = que.front().second;
        que.pop();

        for(int i=1; i<=6; i++)
        {
            int next = now + i; // 다음 좌표
            int tempCnt = count; // 현재 카운트 복사
            if(next == 100) // 100이면 탈출
            {
                cout << ++tempCnt << endl;
                return;
            }
            else if(next < 100)
            {
                if(map[next]!=0) // 뱀이거나 사다리이면 그곳으로 이동
                    next = map[next];
                if(!visited[next]) // 방문하지 않았으면 큐에 삽입
                {
                    que.push({next, ++tempCnt});
                    visited[next] = true;
                }
            }
        }
    }

}

int main()
{
    int x, y;
    cin >> N >> M;
    for(int i=0; i<N+M; i++)
    {
        cin>>x>>y;
        map[x] = y;
    }
    solve();
    return 0;
}
