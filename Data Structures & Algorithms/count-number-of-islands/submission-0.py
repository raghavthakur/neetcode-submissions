'''
'1' is land
'0' is water
grid that is 2D rows and cols
count and return number of islands
from a position there is movement of left, right, top, down

grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]

assume cannot go out of bounds even when checking left, right, top, down

iterate through the rows
iterate through the cols
check if dfs on current position to find adjacent islands
in dfs make sure we are not out of bounds from grid when checking neighbours
track visited positions using tuple of (row,col)
track count of islands
'''
class Solution:
    # runtime: O(row * col)
    # space: O(row * col)
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() # (row, col)
        island_count = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # explore neighbour islands
                if (row, col) not in visited and grid[row][col] == '1':
                    if self.dfs(grid, row, col, visited):
                        island_count += 1

        return island_count

    def dfs(self, grid, r, c, visited):
        stack = [(r,c)] # tuples of positions
        visited.add((r,c))

        while stack:
            row, col = stack.pop()

            # check boundaries and if grid[row][col] is '1' before adding to stack and visited
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
                # left (row, col-1)
                if col > 0 and (row, col-1) not in visited and grid[row][col-1] == '1':
                    stack.append((row, col-1))
                    visited.add((row, col-1))
                # right (row, col+1)
                if col < len(grid[0]) - 1 and (row, col+1) not in visited and grid[row][col+1] == '1':
                    stack.append((row, col+1))
                    visited.add((row, col+1))
                # top (row+1, col)
                if row < len(grid) - 1 and (row+1, col) not in visited and grid[row+1][col] == '1':
                    stack.append((row+1, col))
                    visited.add((row+1, col))
                # bottom (row-1, col)
                if row > 0 and (row-1, col) not in visited and grid[row-1][col] == '1':
                    stack.append((row-1, col))
                    visited.add((row-1, col))

        return True

        