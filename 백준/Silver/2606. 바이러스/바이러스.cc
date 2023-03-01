#include <iostream>
#include <vector>
#define MAX 101

using namespace std;

vector<int> graph[MAX];
bool visited[MAX];
int cnt = 0;
int N,M;

void DFS(int n)
{
    visited[n] = true;
    for(int i=0;i<graph[n].size();i++)
    {
        int now = graph[n][i];
        if(!visited[now])
        {
            DFS(now);
            cnt++;
        }
    }
}


int main()
{
    int a,b;
    cin >> N >> M;
    for(int i=0; i<M; i++)
    {
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    DFS(1);
    cout << cnt << endl;
    return 0;
}


