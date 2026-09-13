'''
'1' is land
'0' is water
values are strings
island surrounded vertically or horizontally --> directions (left, right, up, down)

iterate the rows
iterate the cols
if position at rows and cols == 1 and not in visited
bfs on current position
    use queue to store tuple of position
    add current position to visited
    iterate through queue
    get current position
    for each direction row and col 
        get new direction row and col
        check if new direction is out of bounds, in visited, or == 0 then skip iteration
        otherwise append new direction to queue
        add new direction to visited
increase island count
return island count

Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1
'''
from collections import deque
class Solution:
    # runtime: O(row * col)
    # space: O(row * col)
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        visited = set() # has tuples of (row, col)
        island_count = 0

        def bfs(row, col):
            directions = ((0,-1), (0,1), (-1,0), (1,0)) # left, right, up, down

            queue = deque([(row, col)])
            # add current position to visited
            visited.add((row,col))

            while queue:
                for _ in range(len(queue)):
                    curr_row, curr_col = queue.popleft()

                    for d_row, d_col in directions:
                        new_row, new_col = curr_row + d_row, curr_col + d_col
                        # check if new row and new col is outside bounds
                        if new_row < 0 or new_col < 0 or new_row >= row_len or new_col >= col_len or grid[new_row][new_col] == '0' or (new_row,new_col) in visited:
                            continue # skip the new row and new col since out of bounds
                        queue.append((new_row,new_col))
                        visited.add((new_row,new_col))

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == '1' and (row, col) not in visited:
                    bfs(row, col)
                    island_count += 1
        
        return island_count

'''
Input: grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
Output: 1

{(0,1),(0,0),(0,2),(1,1)}
ic=0
[(0,0),(0,2),(1,1)]
0, 1
(0,0),(0,2)(-1,1),(1,1)
return 1
'''
        