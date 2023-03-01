#include <iostream>

#define MAX 20

using namespace std;

int length, width, height;
int N; // 큐브 개수
int cube[MAX];
// int num[MAX];
bool fail = false;
int cnt = 0;

void input()
{
    cin >> length >> width >> height;
    cin >> N;
    int x,y;   
    for(int i=0;i<N;i++){
        cin >> x >> y;
        cube[x]=y;
    }
}

void solve(int l, int w, int h)
{
    if(l==0 || w==0 || h==0 || fail)
        return ;

    for(int i=N-1; i>=0; i--)
    {
        if(cube[i]==0)
            continue;
        int cur = 1 << i; // 2^n
        
        if(l<cur || w<cur || h<cur)
            continue;

        cube[i]--;
        cnt++;
        solve(l,w,h-cur);
        solve(l-cur,w,cur);
        solve(cur,w-cur,cur);
        return;
    }
    fail = true;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    input();
    solve(length, width, height);

    if(fail)
        cout << "-1";
    else
        cout << cnt;

    return 0;
}