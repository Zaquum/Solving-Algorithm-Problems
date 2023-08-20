class Solution:
    def topologicalSort(self,N,graph,inDegree):
        q = deque()
        for i in range(N):
            if inDegree[i]== 0:
                q.append(i)

        order = []
        while q: 
            u = q.popleft()
            order.append(u)
            for v in graph[u]:
                inDegree[v]-=1 
                if inDegree[v]==0:
                    q.append(v)

        return order

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Order inside a group
        graph = [[]for _ in range(n)]
        inDegree  = [0]*n

        # For items that don't have group we assign an unique group, this allows simpler implementation
        for i in range(n):
            if group[i]==-1:
                group[i] = m
                m+=1

        orderByGroup = [[]for _ in range(m+1)]

        for i in range(n):
            for before in beforeItems[i]:
                if group[before] == group[i]:
                    graph[before].append(i)
                    inDegree[i]+=1


        order = self.topologicalSort(n,graph,inDegree)
        for u in order:
            orderByGroup[group[u]].append(u)

        #Order between groups
        graph = [[]for _ in range(m+1)]
        inDegree  = [0]*(m+1)
        for i in range(n):
            for before in beforeItems[i]:
                if group[before] != group[i]:
                    graph[group[before]].append(group[i])
                    inDegree[group[i]]+=1

        order = self.topologicalSort(m+1,graph,inDegree)
        ans = []
        for group in order: 
            ans+=orderByGroup[group]

        if len(ans)!=n: ans = []
        return ans