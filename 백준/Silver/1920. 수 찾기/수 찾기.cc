#include <iostream>
#include <algorithm>
#include <stdio.h>

using namespace std;

int N,M,x;
void Binary_Search(int x);

int arr[100001];

int main(){
    // ios::sync_with_stdio(0);
    // cin.tie(0);

    // cin>>N;
    scanf("%d",&N);
    for(int i=0;i<N;i++){
        // cin>>x;
        scanf("%d",&x);
        arr[i]=x;
    }
    sort(arr,arr+N);
    // cin>>M;
    scanf("%d",&M);
    for(int i=0;i<M;i++){
        // cin>>x;
        scanf("%d",&x);
        Binary_Search(x);
    }
    return 0;
}

void Binary_Search(int x){
    int start = 0;
    int end = N-1;
    int mid = 0;

    while(end>=start){
        mid = (start+end)/2;

        if(x == arr[mid]){
            // cout<<"1"<<endl;
            printf("1\n");
            return;
        }
        else if(x>arr[mid])
            start = mid + 1;
        else
            end = mid - 1;
    }
    // cout << "0" << endl;
    printf("0\n");
    return;
}