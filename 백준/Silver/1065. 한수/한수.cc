
#include<iostream>

using namespace std;

bool hansoo(int a)
{
    if(a<100)
        return true;
    else if( 100 <= a < 1000)
    {
        int num[3];
        num[2] = a/100;
        num[1] = (a-num[2]*100)/10;
        num[0] = a-num[2]*100-num[1]*10;
        if( num[2]-num[1] == num[1]-num[0])
            return true;
        else
            return false;
    }
    else 
        return false;
}
        
int main(void)
{
    int input;
    int cnt = 0;

    cin >> input;
    for( int i=1 ; i<=input ; i++)
    {
        if(hansoo(i))
            cnt++;
    }
    cout << cnt;
}