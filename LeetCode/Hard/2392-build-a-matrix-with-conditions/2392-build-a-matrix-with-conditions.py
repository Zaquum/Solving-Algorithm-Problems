class Solution:
    def topological_sort(self, k: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * (k + 1)
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        queue = deque([i for i in range(1, k + 1) if indegree[i] == 0])
        topo_order = []
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(topo_order) == k:
            return topo_order
        else:
            return []  # cycle detected

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_order = self.topological_sort(k, rowConditions)
        col_order = self.topological_sort(k, colConditions)
        
        if not row_order or not col_order:
            return []
        
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        
        matrix = [[0] * k for _ in range(k)]
        
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        
        return matrix