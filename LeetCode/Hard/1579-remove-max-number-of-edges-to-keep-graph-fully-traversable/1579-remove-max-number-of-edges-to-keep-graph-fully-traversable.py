# Code from GPT

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU == rootV:
            return False
        if self.rank[rootU] > self.rank[rootV]:
            self.parent[rootV] = rootU
        elif self.rank[rootU] < self.rank[rootV]:
            self.parent[rootU] = rootV
        else:
            self.parent[rootV] = rootU
            self.rank[rootU] += 1
        return True

    def connected_components(self):
        return len(set(self.find(x) for x in range(len(self.parent))))

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_alice = UnionFind(n)
        uf_bob = UnionFind(n)

        edges.sort(reverse=True, key=lambda x: x[0])  # Process type 3 edges first

        removable_edges = 0

        for edge in edges:
            type, u, v = edge
            u -= 1
            v -= 1
            if type == 3:
                if not uf_alice.union(u, v):
                    removable_edges += 1
                else:
                    uf_bob.union(u, v)  # Union for both Alice and Bob
            elif type == 1:
                if not uf_alice.union(u, v):
                    removable_edges += 1
            elif type == 2:
                if not uf_bob.union(u, v):
                    removable_edges += 1

        if uf_alice.connected_components() > 1 or uf_bob.connected_components() > 1:
            return -1

        return removable_edges
