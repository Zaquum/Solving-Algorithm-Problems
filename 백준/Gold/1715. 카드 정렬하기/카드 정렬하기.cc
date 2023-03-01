#include <iostream>
#include <stdio.h>
#include <queue>
#include <functional>

using namespace std;

priority_queue<int, vector<int>, greater<int>> arr;

int min_priority();

int main(){
    int N,x;
    int sum=0;
    cin>>N;
    for(int i=0;i<N;i++){
        cin>>x;
        arr.push(x);
    }
    while(arr.size()>1){
        sum+=min_priority();
    }
    cout<<sum<<endl;
    return 0;
}

int min_priority(){
    int n1 = arr.top();
    arr.pop();
    int n2 = arr.top();
    arr.pop();
    arr.push(n1+n2);
    return n1+n2;
}