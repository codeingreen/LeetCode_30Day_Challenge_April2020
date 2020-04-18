class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
            
        if len(grid) == 0:
            return 0
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "1":
                    grid[i][j] = 'X'
                    
        def bfs(i, j, grid, color):
            
            q = []
            q.append([i,j])
            
            while q:
                
                i, j = q.pop()
                grid[i][j] = color
                
                if i <= len(grid) -2:
                    if grid[i+1][j] == "X":
                        q.append([i+1, j])
                if i > 0:
                    if grid[i-1][j] == "X":
                        q.append([i-1, j])
                if j <= len(grid[0]) -2:
                    if grid[i][j+1] == "X":
                        q.append([i, j+1])
                if j > 0:
                    if grid[i][j-1] == "X":
                        q.append([i, j-1])

            return grid
        
        color = 0
            
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "X":
                    color +=1
                    print('>>', color, i, j)
                    bfs(i, j, grid, color)
       
       
        return color
