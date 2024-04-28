class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        subtree = [0] * n
        dist_sum = [0] * n
        
        @cache
        def dfs(node, parent):
            # itself
            subtree[node] = 1
            
            for neigh in graph[node]:
                if neigh == parent:
                    continue
                dfs(neigh, node)
            
                subtree[node] += subtree[neigh]
                dist_sum[node] += dist_sum[neigh] + subtree[neigh]
        
        dfs(0, -1)
        # print(subtree)
        # print(dist_sum)
        @cache
        def dfs2(node, parent):
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                dist_sum[neighbor] = dist_sum[node] + (n - subtree[neighbor]) - subtree[neighbor]
                dfs2(neighbor, node)
            
        dfs2(0, -1)
        
        return dist_sum