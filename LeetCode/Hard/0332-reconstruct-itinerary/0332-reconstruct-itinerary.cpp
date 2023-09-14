class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, vector<string>> graph;
        
        // Step 1: Construct the graph with tickets in sorted order
        for(const auto& ticket : tickets) {
            graph[ticket[0]].push_back(ticket[1]);
        }

        // greater<자료형>() : 내림차순, less<자료형>() : 오름차순
        for(auto& item : graph) {
            sort(item.second.begin(), item.second.end(), greater<string>());
        }
    
        vector<string> route;
        
        // Step 2 and 3: Define recursive DFS function
        visit("JFK", graph, route);
        
        // Step 5: The result is in reverse order, so return the reversed vector
        reverse(route.begin(), route.end());
        return route;
    }
    
private:
    void visit(const string& airport, 
               unordered_map<string, vector<string>>& graph, 
               vector<string>& route) {
        while(!graph[airport].empty()) {
            string next_airport = graph[airport].back();
            graph[airport].pop_back();
            
            // Step 3 and 4: Recursive call to visit other airports 
            // and backtracking when no further path
            visit(next_airport, graph, route);
        }
        
        // Adding the airport to the route when no unvisited neighbors left
        route.push_back(airport);
    }
};