#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define MAX 100001

using namespace std;
using ll=long long;
int N;
int cnt=0;

struct lecture
{
    int id;
    ll start;
    ll end;
    lecture(int a, ll b, ll c) : id(a), start(b), end(c) {}
    
    inline bool operator> (const lecture& lecture_) const
    {
        // return this->start > lecture_.start;
        return this->end > lecture_.end;
    }
    inline bool operator< (const lecture& lecture_) const
    {
        return this->start < lecture_.start;
    }
};


vector<lecture> lectures;
priority_queue<lecture, vector<lecture>, greater<lecture>> que;
vector<int> room;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    room.reserve(N+1);
    int x;
    ll y,z;

    for(int i=0;i<N;i++)
    {
        cin >> x >> y >> z;
        lectures.push_back(lecture(x,y,z));
        // cout << i.id << " ";
    }
    // for(int i=0;i<lectures.size();i++)
    //     cout << i.id << " ";
    sort(lectures.begin(),lectures.end());
    // for(int i=0;i<lectures.size();i++)
    //     cout << i.id << " ";
    for(auto i : lectures)
    {
        if(!que.empty() && (que.top().end <= i.start))
        {
            room[i.id] = room[que.top().id];
            que.pop();
        }
        else
        {
            cnt++;
            room[i.id] = cnt;
        }
        que.push(i);
    }
    cout << cnt << endl;
    for(int i=1;i<=N;i++)
    {
        cout << room[i] << "\n";
    }
    return 0;
}