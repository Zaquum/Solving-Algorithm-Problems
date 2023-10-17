class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0] * n
        
        for i in range(n):
            if leftChild[i] != -1:
                indegree[leftChild[i]] += 1
            if rightChild[i] != -1:
                indegree[rightChild[i]] += 1
        
        # If any node has an in-degree not equal to 1, return False.
        if indegree.count(0) != 1 or indegree.count(1) != n-1:
            return False

        root = indegree.index(0)
        
        visited = set()
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            if leftChild[node] != -1:
                dfs(leftChild[node])
            if rightChild[node] != -1:
                dfs(rightChild[node])
                
        dfs(root)
        
        return len(visited) == n