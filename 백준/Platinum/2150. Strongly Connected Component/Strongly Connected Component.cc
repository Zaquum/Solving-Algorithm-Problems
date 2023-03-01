#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
#define MAX 10001

using namespace std;

bool visited[MAX];
int V, E;
vector<vector<int>> result;
vector<int> scc;
vector<int> graph[MAX];
vector<int> rev_graph[MAX];
stack<int> stack_seq;

void SCC();
void DFS(int);
void rev_DFS(int);

int main(){
    int u,v;
    cin>>V>>E;
    for(int i=0;i<E;i++){
        cin>>u>>v;
        graph[u].push_back(v);
        rev_graph[v].push_back(u);
    }

    SCC();
    
    return 0;
}

void SCC(){
    for(int i=1;i<=V;i++){
        if(!visited[i])
            DFS(i);
    }
    for(int i=1;i<=V;i++)
        visited[i]=false;
    while(!stack_seq.empty()){
        int now = stack_seq.top();
        stack_seq.pop();
        if(visited[now])
            continue;
        rev_DFS(now);
        sort(scc.begin(),scc.end());
        result.push_back(scc);
        scc.clear();
    }
    sort(result.begin(),result.end());
    cout<<result.size()<<endl;
    for(int i=0; i<result.size();i++){
        for(int j=0;j<result[i].size();j++)
            cout << result[i][j] << " ";
        cout << "-1" << endl;
    }
}

void DFS(int u){
    visited[u] = true;
    for(int v=0; v<graph[u].size(); v++){
        int next = graph[u][v];
        if(!visited[next])
            DFS(next);
    }
    stack_seq.push(u);
}

void rev_DFS(int u){
    visited[u] = true;
    for(int i=0;i<rev_graph[u].size(); i++){
        int next = rev_graph[u][i];
        if(!visited[next])
            rev_DFS(next);
    }
    scc.push_back(u);
}