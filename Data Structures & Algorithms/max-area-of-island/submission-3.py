'''
0 is water
1 is land

island connected with group 1's horizontally or vertically (left, right, top, down)
grid surrounded by water (check within bounds)

return max number of cells within island

grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

iterate grid with row and col loops
check if curr position is grid with 1
run dfs on curr position and explore neighbours on left, right, top, down
check if neighbours are within bounds and grid with 1
track max cells per island
return island with the most cells
'''
class Solution:

    # runtime: O(row * col) since traverse row and col on grid
    # space: O(row * col) since visited and stack contains all elements in worst case of all 1's on grid
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        visited = set()
        max_island = 0

        def dfs(r, c, visited):
            # base case inbounds
            if r < 0 or c < 0 or r >= row_len or c >= col_len:
                return 0

            # base case wrong value
            if grid[r][c] != 1:
                return 0
        
            # base case visited
            if (r, c) in visited:
                return 0
            visited.add((r, c))
            
            # left (0, -1), right (0, 1), top (-1, 0) down (1, 0)
            return 1 + dfs(r, c - 1, visited) + dfs(r, c + 1, visited) + dfs(r - 1, c, visited) + dfs(r + 1, c, visited) 


        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1 and (row, col) not in visited:
                    # return cell count per dfs on islands
                    max_island = max(max_island, dfs(row, col, visited))
        
        return max_island