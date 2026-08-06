class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src,dst in tickets:
            heapq.heappush(graph[src],dst)
        
        route = []

        def dfs(u:str)-> None:
            heap = graph[u]
            while heap:
                v=heapq.heappop(heap)
                dfs(v)
            route.append(u)
        
        dfs('JFK')
        return route[::-1]