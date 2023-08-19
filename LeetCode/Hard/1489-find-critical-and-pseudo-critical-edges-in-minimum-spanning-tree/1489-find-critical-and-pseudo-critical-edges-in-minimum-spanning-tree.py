class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Adding index to the edges to keep track of original indices
        for i, edge in enumerate(edges):
            edges[i].append(i)
        # Sorting the edges by weight
        edges.sort(key=lambda x: x[2])

        def find(parents, x):
            if parents[x] != x:
                parents[x] = find(parents, parents[x])
            return parents[x]

        def kruskal(exclude=-1, include=-1):
            parents = [i for i in range(n)]
            rank = [0] * n
            cost = 0
            numEdges = 0
            
            if include != -1:
                a, b, weight, _ = edges[include]
                parents[find(parents, a)] = find(parents, b)
                cost += weight
                numEdges += 1
            
            for i, (a, b, weight, index) in enumerate(edges):
                if i == exclude:
                    continue
                parentA = find(parents, a)
                parentB = find(parents, b)
                if parentA != parentB:
                    if rank[parentA] < rank[parentB]:
                        parents[parentA] = parentB
                    else:
                        parents[parentB] = parentA
                        if rank[parentA] == rank[parentB]:
                            rank[parentA] += 1
                    cost += weight
                    numEdges += 1
                    if numEdges == n - 1:
                        break
            return cost if numEdges == n - 1 else float('inf')

        minCost = kruskal()
        criticalEdges = []
        pseudoCriticalEdges = []

        for i, edge in enumerate(edges):
            if kruskal(exclude=i) > minCost:
                criticalEdges.append(edge[3])
            elif kruskal(include=i) == minCost:
                pseudoCriticalEdges.append(edge[3])

        return [criticalEdges, pseudoCriticalEdges]

