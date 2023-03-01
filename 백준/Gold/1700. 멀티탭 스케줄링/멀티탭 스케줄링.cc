#include <iostream>
#include <algorithm>
#include <stack> 
#include <queue>

using namespace std;

int N,K;
int cnt=0;
int queue_[100];
bool plug_in[100]={false};

vector<int> plug;

void input()
{
    cin >> N >> K;
    int x;
    for(int i=0;i<K;i++)
    {
        cin >> queue_[i];
    }
}

// int solve()
// {

//     // for(auto i : queue_)
//     // {
//     //     //1. 빈 곳이 있는 경우
//     //     if(arr.size()<N)
//     //     {
//     //         arr.push_back(i);
//     //         continue;
//     //     }
//     //     //2. 플러그인에 꽂혀있으면 패스
//     //     auto find_it = find(arr.begin(),arr.end(),i);
//     //     //3. 없으면 마지막 걸 빼기
//     //     if(find_it == arr.end())
//     //     {
//     //         *(arr.end()-1) = *find_it;
//     //         cnt++;
//     //     }
//     // }
// }

int find_plug(int x)
{
    int last = 0;
    for(auto i : plug)
    {
        int idx = -1;
        for(int j=x; j<K; j++)
        {
            if(queue_[j]==i) // 쓸 예정이 있음
            {
                idx=j;
                break;
            }
        }
        if(idx==-1) return i; // 쓸 예정이 없으면 이 플러그를 빼자
        else last = max(last, idx); // 가장 나중에 사용되는 플러그
    }
    return queue_[last];
}

void solve()
{
    for(int i=0; i<K; i++)
    {
        int cur = queue_[i];
        
        if(plug_in[cur]) 
            continue;
        
        if(N>0)
        {
            plug_in[cur] = true;
            plug.push_back(cur);
            N--;
        }
        else
        {
            int find_it = find_plug(i);
            plug.erase(remove(plug.begin(),plug.end(), find_it), plug.end());
            plug_in[find_it] = false;
            plug_in[cur] = true;
            plug.push_back(cur);
            cnt++;
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    input();
    solve();
    cout<<cnt;
    return 0;
}
