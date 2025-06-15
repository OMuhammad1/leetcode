class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        visited = set()

        for u, v in prerequisites:
            if u not in adj:
                adj[u] = []
            adj[u].append(v)
        
        def dfs(crs):
            if crs not in adj or adj[crs] == []:
                return True 
            if crs in visited:
                return False
            
            visited.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            adj[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
