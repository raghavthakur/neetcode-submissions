'''
0 is water
1 is land
island is group of 1's connected horziontally or vertically 
assume edges of grid surrounded by water 


area = number of connected positions on grid
return max area otherwise return 0

constraints
- neighbours which are (left, right, top, down)
- cannot exceed bounds of grid

grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

iterate through the grid using for loops for row and col
for each position in the grid use bfs to find all the connected positions/components
track the the largest island and return it
for bfs need to check neighbours of left, right, top, down
for bfs when checking neighbours we cannot exceed bounds of grid
for bfs when checking neighbours we cant to check for positions with grid value 1

'''
from collections import deque

class Solution:
    # runtime: O(row * col) due to iteration of grid and not visiting cell twice
    # space: O(row * col) due to visited and queue worst case having entire grid of 1's
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # left, right, top, down
        row_len = len(grid)
        col_len = len(grid[0])

        visited = set() # contains position tuples
        largest_island = 0

        def bfs(r, c):
            queue = deque([(r, c)]) # (row, col) tuple
            visited.add((r, c))

            cell_count = 1

            while queue:
                for _ in range(len(queue)):
                    qr, qc = queue.popleft()

                    # directions for neighbours
                    for dr, dc in directions:
                        nr, nc = dr + qr, dc + qc

                        # cannot exceed bounds
                        if nr < 0 or nc < 0 or nr >= row_len or nc >= col_len or grid[nr][nc] != 1 or (nr, nc) in visited:
                            continue # skip the current neighbour
                        
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        cell_count += 1

            return cell_count




        # iterate through the grid
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1 and (row, col) not in visited:
                    largest_island = max(largest_island, bfs(row, col))
        
        return largest_island






