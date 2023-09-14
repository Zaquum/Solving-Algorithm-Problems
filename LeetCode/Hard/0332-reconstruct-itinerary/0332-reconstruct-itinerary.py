class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for dep, arr in sorted(tickets, key= lambda x:x[1], reverse=True):
            graph[dep].append(arr)
            # print(dep, " and ", arr)
        
        # print(graph)
        route = []
        
        def visit(airport):
            while graph[airport]:
                visit(graph[airport].pop())
            route.append(airport)
        
        visit('JFK')
        
        return route[::-1]