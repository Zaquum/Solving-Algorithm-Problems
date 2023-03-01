#include <iostream>
#include <vector>
#include <queue>
#define MAX 32001

using namespace std;

int N,M;
int cnt[MAX];
vector<int> arr[MAX];

void solve();

int main(){
    cin >> N >> M;
    for(int i=0; i<M; i++){
        int A,B;
        cin >> A >> B;
        arr[A].push_back(B);
        cnt[B]++;
    }
    solve();

    return 0;
}

void solve(){
    priority_queue<int, vector<int>, greater<int>> que; // min-heap
    
    for(int i=1;i<=N;i++)
        if(!cnt[i]) 
            que.push(i);
    while(!que.empty())
    {
        int now = que.top();
        que.pop();
        cout << now << " ";
        for(auto neigh : arr[now])
            if(!--cnt[neigh])
                que.push(neigh);
    }
}