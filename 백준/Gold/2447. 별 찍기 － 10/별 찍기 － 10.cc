#include <iostream>

using namespace std;

int N,k;
int cnt = 0;


void print_star(int i, int j, int n)
{
    if(n==1) // 정사각형의 크기가 1이면 *출력
        cout << "*";
    else if( (i/(n/3))%3 == 1 && (j/(n/3))%3 == 1) // 공백인 칸
        cout << " ";
    else // 발견하지 못했다면 작은 정사각형에서 확인
        print_star(i,j,n/3);

}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<N;j++)
        {
            print_star(i,j,N);
        }
        cout<<endl;
    }
    return 0;
}