#include <iostream>
#include <vector>
#define MAX 10001
#include <algorithm>
using namespace std;

vector<int> friend_[MAX];
int money[MAX];
bool visited[MAX] = {false};
int N,M, k;
int cnt = 0;

void input()
{
    cin >> N >> M >> k;
    for(int i=1;i<=N;i++)
        cin >> money[i];
    int x,y;
    for(int i=0;i<M;i++)
    {
        cin >> x >> y;
        friend_[x].push_back(y);
        friend_[y].push_back(x); 
    }
}

// int solve()
// {
//     for(int i=0;i<N;i++)
//     {
//         int minimum = 10000000;
//         if(!visited[i])
//         {
//             visited[i]=true;
//             if(minimum >= money[i])
//                 minimum = money[i];
//             if(friend_[i].size())
//             {
//                 for(int j=0;j<friend_[i].size();j++)
//                 {
//                     visited[j] = true;
//                     if(minimum >= money[j])
//                         minimum = money[j];
//                 }
//             }
//             cnt+=minimum;
//         }
//     }
//     return cnt;
// }

int DFS(int n, int minimum)
{
    if(!visited[n])
    {
        visited[n] = true;
        for(auto next : friend_[n])
        {
            if(visited[next])
                continue;
            int next_min = min(minimum, money[next]);
            minimum = DFS(next, next_min);
        }
        return min(minimum, money[n]);
    }
    // return cnt;
}


int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    input();
    // cout << solve();
    int minimum = 10000000;
    for(int i=1;i<=N;i++)
    {
        // cout << DFS(i,minimum) << " " << money[i] << endl;
        if(visited[i])
            continue;
        cnt += DFS(i,minimum);
    }
    if(k >= cnt)
        cout << cnt;
    else
        cout << "Oh no";
    return 0;
}