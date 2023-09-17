class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        # d = [[float('inf')]*n for _ in range(n)]

        # for i in range(n):
        #     d[i][i] = 0

        # for i, x in enumerate(graph):
        #     for j in x:
        #         d[i][j] = 1
        #         d[j][i] = 1

        # for k in range(n):
        #     for i in range(n):
        #         for j in range(n):
        #             if d[i][k] + d[k][j] < d[i][j]:
        #                 d[i][j] = d[i][k] + d[k][j]
        
        # memo = {}

        # def find_shortest_path(curr_node, visited_nodes, path_length):
        #     if len(visited_nodes) == n:
        #         return path_length
            
        #     if (curr_node, tuple(visited_nodes)) in memo:
        #         return memo[(curr_node, tuple(visited_nodes))]

        #     res = min(
        #         find_shortest_path(next_node, visited_nodes + [next_node], path_length + d[curr_node][next_node])
        #         for next_node in range(n)
        #         if next_node not in visited_nodes
        #     )

        #     memo[(curr_node, tuple(visited_nodes))] = res
        #     return res

        # return min(find_shortest_path(i, [i], 0) for i in range(n))
        memo = {}
        
        def helper(mask, node):
            if mask == (1 << n) - 1:
                return 0
            if (mask, node) in memo:
                return memo[(mask, node)]

            res = float('inf')
            for v in range(n):
                if not (mask >> v) & 1:
                    res = min(res, 1 + helper(mask | (1 << v), v))

            memo[(mask, node)] = res
            return res
        
        return min(helper(1 << i, i) for i in range(n))