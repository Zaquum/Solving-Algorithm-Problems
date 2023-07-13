class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        #adj matrix
        for i, j in prerequisites:
            graph[i].append(j)
        
        def dfs(cur: int):
            # visited
            # not visite : 0 / visited already : 1 / visit now : -1
            if visited[cur] == 1:
                return True
            if visited[cur] == -1:
                return False

            # now visit it
            visited[cur] = -1

            for pre in graph[cur]:
                if dfs(pre) == False:
                    return False

            # finish dfs and visit already
            visited[cur] = 1
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True