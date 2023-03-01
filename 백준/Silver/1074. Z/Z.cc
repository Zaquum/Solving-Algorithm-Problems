#include <iostream>

using namespace std;

int N,r,c;
int cnt = 0;
void solve(int i, int j, int n)
{
    if(i==r&&j==c)
    {
        cout << cnt << endl;
        return;
    }

    if(r < i + n && r>=i && c < j+n && c>=j)
    {
        solve(i,j,n/2);
        solve(i,j+n/2,n/2);
        solve(i+n/2,j,n/2);
        solve(i+n/2,j+n/2,n/2);
    }

    else
        cnt += n*n;
}

int main()
{
    cin >> N >> r >> c;
    solve(0,0,(1<<N));
    return 0;
}