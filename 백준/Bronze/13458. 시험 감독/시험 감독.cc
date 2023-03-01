#include <bits/stdc++.h>
using namespace std;
#define MAX 1000000

int N,B,C;
int A[MAX];

void Input()
{
	cin>>N;
	for(int i=0;i<N;i++)
		cin>>A[i];
	cin>>B>>C;
}

int Ob_1(int x)
{
	int cnt;
	int a=A[x]-B;
	if(a<=0)
		return 1;
	cnt=a/C+1;
	if(a%C!=0)
		cnt++;
	return cnt;
}

int main() {
	// your code goes here
	Input();
	long long cnt_total=0;
	
	for(int i=0;i<N;i++)
		cnt_total+=Ob_1(i);
		
	cout<<cnt_total<<endl;
	return 0;
}