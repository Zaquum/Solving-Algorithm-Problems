#include<iostream>

using namespace std;

int main(void)
{
    int V, A, B;
    int total = 0;
    int cnt = 0;

    cin >> A >> B >> V;
    
        if((1<=B) && (B<A) && (A<=V) && (V<=1000000000))
        {
            cnt = (V-B-1)/(A-B)+1;
        }
    cout << cnt << endl;
    return 0;
}
