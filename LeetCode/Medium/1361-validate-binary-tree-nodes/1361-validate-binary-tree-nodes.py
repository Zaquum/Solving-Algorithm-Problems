class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Step 1: Find the parent for each node
        parent = [-1] * n  # -1 indicates no parent
        for i in range(n):
            if leftChild[i] != -1:
                # if this node already has a parent, it's not a valid tree
                if parent[leftChild[i]] != -1:
                    return False
                parent[leftChild[i]] = i
            if rightChild[i] != -1:
                # if this node already has a parent, it's not a valid tree
                if parent[rightChild[i]] != -1:
                    return False
                parent[rightChild[i]] = i

        # Step 2: Check the number of nodes with no parents
        root_count = parent.count(-1)
        if root_count != 1:
            return False

        # Step 3: Ensure all nodes are connected
        visited = [False] * n
        stack = [parent.index(-1)]  # start DFS from the root

        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            if leftChild[node] != -1:
                stack.append(leftChild[node])
            if rightChild[node] != -1:
                stack.append(rightChild[node])

        return all(visited)
        
        # indegree = [0] * n
        
        # for i in range(n):
        #     if leftChild[i] != -1:
        #         indegree[leftChild[i]] += 1
        #     if rightChild[i] != -1:
        #         indegree[rightChild[i]] += 1
        
        # # If any node has an in-degree not equal to 1, return False.
        # if indegree.count(0) != 1 or indegree.count(1) != n-1:
        #     return False

        # root = indegree.index(0)
        
        # visited = set()
        
        # def dfs(node):
        #     if node in visited:
        #         return
        #     visited.add(node)
        #     if leftChild[node] != -1:
        #         dfs(leftChild[node])
        #     if rightChild[node] != -1:
        #         dfs(rightChild[node])
                
        # dfs(root)
        
        # return len(visited) == n