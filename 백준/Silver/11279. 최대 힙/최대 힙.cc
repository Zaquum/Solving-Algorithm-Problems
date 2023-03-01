#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <functional>
using namespace std;

priority_queue<int,vector<int>, less<int>> arr;

void max_heap(int);

int main(){
    int N,x;
    scanf("%d", &N);
    for(int i=0;i<N;i++){
        scanf("%d",&x);
        max_heap(x);
    }
    return 0;
}

void max_heap(int x){
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