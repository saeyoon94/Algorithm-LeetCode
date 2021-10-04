class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        visited = [False] * numCourses
        
        for prerequsite in prerequisites :
            indegree[prerequsite[0]] += 1
            graph[prerequsite[1]].append(prerequsite[0])
        
        q = deque()
        
        for i, val in enumerate(indegree) :
            if val == 0 :
                q.append(i)
                visited[i] = True
                
        if len(q) == 0 :
            return False
                
        while len(q) > 0 :
            now = q.popleft()
            
            for child in graph[now] :
                indegree[child] -= 1
                
                if indegree[child] == 0 and not visited[child] :
                    q.append(child)
                    visited[child] = True
        
        for v in visited :
            if not v :
                return False
        return True