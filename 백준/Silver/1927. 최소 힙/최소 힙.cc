#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <functional>
using namespace std;

priority_queue<int,vector<int>, greater<int>> arr;

void min_heap(int);

int main(){
    int N,x;
    scanf("%d", &N);
    for(int i=0;i<N;i++){
        scanf("%d",&x);
        min_heap(x);
    }
    return 0;
}

void min_heap(int x){
    if(!x){
        if(!arr.empty()){
            printf("%d\n", arr.top());
            arr.pop(); 
        }
        else{
            printf("0\n");
        }
    }
    else
        arr.push(x);
}