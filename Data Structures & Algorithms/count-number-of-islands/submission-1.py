class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        visited = set()

        # iterate through the grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # dfs to find all neighbouring lands before increment island_count
                if self.dfs(grid, row, col, visited):
                    # increase count for island found
                    island_count += 1

        
        return island_count
    
    def dfs(self, grid, r, c, visited):
        # base case for inbounds
        row_inbound = 0 <= r < len(grid)
        col_inbound = 0 <=c < len(grid[0])
        
        if not row_inbound or not col_inbound:
            return False 

        # base case for position being land '1'
        if grid[r][c] != '1':
            return False

        # base case for visited position
        if (r,c) in visited:
            return False

        visited.add((r,c))

        # recursive call for left, right, top, bottom
        self.dfs(grid, r, c-1, visited)
        self.dfs(grid, r, c+1, visited)
        self.dfs(grid, r-1, c, visited)
        self.dfs(grid, r+1, c, visited)

        return True

        