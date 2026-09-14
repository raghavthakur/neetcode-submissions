'''
input: 
grid of mxn rows and cols
0 is water
1 is land
island is group of 1's connected horizontally or vertically

output:
max area of an island in grid
otherwise return 0

Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

Output: 6

iterate rows
iterate cols
for each value in the grid check if it's == 1 and check position not in visited
call bfs to find area of island
    in bfs use queue
    track area
    add current position to visited
    iterate on queue
    get current position
    for each direction
    check if new position is out of bounds or not in visited or not == 1
    skip new position if out of bounds
    append to queue
    add to visited
    return area
update max area of island
return max area of island

'''
# runtime: O(n x m) where n is length of rows and m is length of cols
# space: O(n x m)
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        max_area = 0

        visited = set()


        def bfs(r, c):
            directions = [(0,-1),(0,1),(-1,0),(1,0)] # left, right, up, down
            area = 1

            queue = deque([(r,c)])
            visited.add((r,c))

            while queue:
                for _ in range(len(queue)):
                    curr_row, curr_col = queue.popleft()

                    for d_row, d_col in directions:
                        new_row, new_col = curr_row + d_row, curr_col + d_col
                        # out of bounds
                        if new_row < 0 or new_col < 0 or new_row >= row_len or new_col >= col_len or grid[new_row][new_col] == 0 or (new_row,new_col) in visited:
                            continue # skip new position
                        area += 1
                        queue.append((new_row,new_col))
                        visited.add((new_row,new_col))
            return area
            

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1 and (row,col) not in visited:
                    max_area = max(max_area, bfs(row, col))
        
        return max_area



















