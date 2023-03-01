#include <bits/stdc++.h>
using namespace std;
#define MAX 100

int N;
int arr[MAX];
int op[4];
int result_max=-1000000000;
int result_min=1000000000;
int PLUS,MINUS,MULTIPLY,DIVISION;
int cnt=0;

int get_max(int a,int b){
	return a>b?a:b;
}

int get_min(int a,int b){
	return a<b?a:b;
}

void Input(){
	cin>>N;
	for(int i=0;i<N;i++)
		cin>>arr[i];
	cin>>PLUS>>MINUS>>MULTIPLY>>DIVISION;
}

void solution(int Sum, int n, int pl, int mi, int multi, int div){
	if(pl>0){
		solution(Sum+arr[n],n+1,pl-1,mi,multi,div);
//		result_max=get_max(result_max,a);
//		result_min=get_min(result_min,a);
	}
	if(mi>0){
		solution(Sum-arr[n],n+1,pl,mi-1,multi,div);
//		result_max=get_max(result_max,b);
//		result_min=get_min(result_min,b);
	}
	if(multi>0){
		solution(Sum*arr[n],n+1,pl,mi,multi-1,div);
//		result_max=get_max(result_max,c);
//		result_min=get_min(result_min,c);
	}
	if(div>0){
		solution(Sum/arr[n],n+1,pl,mi,multi,div-1);
//		result_max=get_max(result_max,d);
//		result_min=get_min(result_min,d);	
	}
	if(pl==0&&mi==0&&multi==0&&div==0){
		result_max=get_max(result_max,Sum);
		result_min=get_min(result_min,Sum);
		return;
	}
}

int main() {
	// your code goes here
	Input();
	solution(arr[0],1,PLUS,MINUS,MULTIPLY,DIVISION);
	cout<<result_max<<endl<<result_min<<endl;
	return 0;
}