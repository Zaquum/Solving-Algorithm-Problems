#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> arr;
int N,x;

int GCD(int a, int b)
{
    return (a%b? GCD(b, a%b) : b);
}

int max_sum(int start, int end)
{
    if(start == end) // 배열의 크기가 1이면 본인 반환
        return arr[start];
    
    int mid = (end-start+1)/2;
    // 왼쪽
    int left_gcd = arr[start]; // 왼쪽 스타트
    // 왼쪽 GCD 구하기
    for(int i=start+1; i<start+mid ; i++)
    {
        left_gcd = GCD(arr[i], left_gcd);
    }
    int left_sum = max_sum(start + mid, end) + left_gcd; // 나머지도 구하라!
    // 오른쪽
    int right_gcd = arr[end]; // 오른쪽 스타트 - 끝부터
    // 오른쪽 GCD 구하기
    for(int i=end-1; i>=start+mid; i--)
    {
        right_gcd = GCD(right_gcd, arr[i]);
    }
    int right_sum = max_sum(start, start + mid -1) + right_gcd; // 나머지도 구해

    return max(left_sum, right_sum); // 최대값 반환
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin >> N;
    for(int i=0;i<N;i++)
    {
        cin >> x;
        arr.push_back(x);
    }
    cout << max_sum(0,arr.size()-1) << endl;
    return 0;
}
