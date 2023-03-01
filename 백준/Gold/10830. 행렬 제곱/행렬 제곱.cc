#include <iostream>
#define MAX 1000
using namespace std;

int N,x;
long long B;

long long matrix[5][5], temp[5][5], ans[5][5];

void matrix_pow(long long a[5][5], long long b[5][5])
{
    for(int i=0;i<N;i++)
        for(int j=0;j<N;j++)
        {
            for(int k=0;k<N;k++)
            {
                temp[i][j] += (a[i][k]*b[k][j]);
            }
            temp[i][j] %= MAX;
        }
        
    for(int i=0;i<N;i++)
        for(int j=0;j<N;j++)
        {
            b[i][j]=temp[i][j];
            temp[i][j] = 0;
        }
}

void solve(long long b)
{
    while(b>0)
    {
        if(b%2)
            matrix_pow(matrix,ans);
        matrix_pow(matrix,matrix);
        b/=2;
    }
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    //input;
    cin >> N >> B;
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
            cin >> matrix[i][j];
        }
        ans[i][i] = 1;
    }
    solve(B);
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
            cout << ans[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}