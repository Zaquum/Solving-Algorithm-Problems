#include <iostream>
#include <vector>
// #include <algorithm>
#define MAX 1000001

using namespace std;

int N, M;
vector<int> map[MAX];
bool visited[MAX];
int adaptor[MAX][2]; // 0 : 얼리어답터, 1 : 일반인

void solve(int root);

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> N;
    int a,b;
    for(int i=0; i<N-1; i++)
    {
        cin>>a>>b;
        map[a].push_back(b);
        map[b].push_back(a);
    }
    solve(1);
    
    cout << min(adaptor[1][0], adaptor[1][1]);
    return 0;
}

void solve(int root)
{
    visited[root] = true;
    adaptor[root][0] = 1;
    
    for(int i=0; i<map[root].size(); i++)
    {
        int next = map[root][i];
        if(visited[next])
            continue;
        solve(next);
        adaptor[root][1]+=adaptor[next][0];
        adaptor[root][0]+=min(adaptor[next][0],adaptor[next][1]);
    }
}