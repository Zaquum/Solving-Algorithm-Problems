class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        degree = [0] * n
        # destination 제외
        # source들은 0
        for edge in edges:
            degree[edge[1]] += 1
        ans = []
        for i in range(n):
            if degree[i] == 0:
                ans.append(i)
        return ans