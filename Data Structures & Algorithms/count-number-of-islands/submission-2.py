'''
'1' is land
'0' is water
count and return number of islands
adjacent lands horizontally and vertically left, right, top, down


grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]

iterate through grid for rows and cols
check if current position (row, col) == '1'
if so then use bfs to check neigbour lands to be island
count number of islands and return
'''
from collections import deque

# runtime: O(row * col) since for loops visit each position on grid
# space: O(row * col) because visited and stack contains all positions in worst case if all lands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [(0, -1), (0, 1), (-1, 0), (1, 0)] # (row, col)
        row_len = len(grid)
        col_len = len(grid[0])
        island_count = 0
        visited = set() # contains (row, col)

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))

            while queue:
                for _ in range(len(queue)):
                    qr, qc = queue.popleft()

                    # for each direction of neighbour
                    for dr, dc in direction:
                        new_r, new_c = qr + dr, qc + dc

                        # out of bounds or not '1' or visited
                        if new_r < 0 or new_r >= row_len or new_c < 0 or new_c >= col_len or grid[new_r][new_c] != '1' or (new_r, new_c) in visited:
                            continue # skip this neighbour
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))


        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row, col)
                    island_count += 1
        
        return island_count
        