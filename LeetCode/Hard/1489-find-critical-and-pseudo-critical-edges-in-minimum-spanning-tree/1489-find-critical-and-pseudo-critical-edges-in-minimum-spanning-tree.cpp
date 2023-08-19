class Solution {
public:
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        for (int i = 0; i < edges.size(); ++i) {
            edges[i].push_back(i);
        }

        std::sort(edges.begin(), edges.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[2] < b[2];
        });

        int minCost = kruskal(n, edges);
        std::vector<int> criticalEdges, pseudoCriticalEdges;

        for (int i = 0; i < edges.size(); ++i) {
            if (kruskal(n, edges, i) > minCost) {
                criticalEdges.push_back(edges[i][3]);
            } else if (kruskal(n, edges, -1, i) == minCost) {
                pseudoCriticalEdges.push_back(edges[i][3]);
            }
        }

        return { criticalEdges, pseudoCriticalEdges };
    }

    int find(std::vector<int>& parents, int x) {
        if (parents[x] != x) {
            parents[x] = find(parents, parents[x]);
        }
        return parents[x];
    }

    int kruskal(int n, std::vector<std::vector<int>>& edges, int exclude = -1, int include = -1) {
        std::vector<int> parents(n), rank(n, 0);
        for (int i = 0; i < n; ++i) parents[i] = i;

        int cost = 0, numEdges = 0;

        if (include != -1) {
            int a = edges[include][0], b = edges[include][1], weight = edges[include][2];
            parents[find(parents, a)] = find(parents, b);
            cost += weight;
            numEdges += 1;
        }

        for (int i = 0; i < edges.size(); ++i) {
            if (i == exclude) continue;
            int a = edges[i][0], b = edges[i][1], weight = edges[i][2];
            int parentA = find(parents, a), parentB = find(parents, b);
            if (parentA != parentB) {
                if (rank[parentA] < rank[parentB]) {
                    parents[parentA] = parentB;
                } else {
                    parents[parentB] = parentA;
                    if (rank[parentA] == rank[parentB]) {
                        rank[parentA] += 1;
                    }
                }
                cost += weight;
                numEdges += 1;
                if (numEdges == n - 1) break;
            }
        }

        return numEdges == n - 1 ? cost : INT_MAX;
    }

};