class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = set()
        visited = set()

        def dfs(node: int) -> bool:
            if node in safe_nodes:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            # if there is any path that does not lead to a terminal node, the node is not safe
            if any(not dfs(neigh) for neigh in graph[node]):
                return False

            # node is safe
            safe_nodes.add(node)
            return True

        return sorted(node for node in range(len(graph)) if dfs(node))