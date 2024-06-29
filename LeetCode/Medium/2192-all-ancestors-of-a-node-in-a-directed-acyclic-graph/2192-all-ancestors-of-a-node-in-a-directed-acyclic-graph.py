class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Code from GPT
        
        # Step 1: Initialize the adjacency list for the graph
        graph = [[] for _ in range(n)]
        for edge in edges:
            from_node, to_node = edge
            graph[to_node].append(from_node)

        # Step 2: Initialize the answer list
        answer = [[] for _ in range(n)]

        # Step 3: Define a DFS function to find ancestors
        def dfs(node, ancestors):
            for parent in graph[node]:
                if parent not in ancestors:
                    ancestors.append(parent)
                    dfs(parent, ancestors)

        # Step 4: Run DFS for each node to find ancestors
        for i in range(n):
            dfs(i, answer[i])
            answer[i].sort()  # Sort ancestors in ascending order

        return answer