class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [0] * n
        path = [0] * n

        def dfs(cur: int, visited, path):
            visited[cur] = 1
            path[cur] = 1
            for node in graph[cur]:
                if visited[node] == 0:
                    if dfs(node,visited,path):
                        return True
                elif path[node]:
                    return True
            path[cur] = 0
            return False

        ans = []

        for i in range(n):
            if visited[i] == 0:
                dfs(i, visited, path)
        for i in range(n):
            if path[i] == 0:
                ans.append(i)
        return ans