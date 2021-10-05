class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        
        for i in range(m) :
            for j in range(n) :
                if grid[i][j] == '1' :
                    self.dfs(i, j, grid, m, n)
                    count += 1
        return count
        
    
    def dfs(self, r, c, grid, m, n) :
        
        stack = [(r,c)]
        grid[r][c] = '-1'
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        
        while stack :
            r, c = stack.pop()
            
            for i in range(4) :
                nx, ny = r+dx[i], c+dy[i]
                
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny]=='1' :
                    grid[nx][ny] = '-1'
                    stack.append((nx, ny))
                     
                        
                    
                    
            
            
        
        
    
