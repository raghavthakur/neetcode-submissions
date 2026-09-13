class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        visited = set() # tuple of (row, col)
        max_area = 0
		
        def bfs(row, col):
            queue = deque([(row, col)])
            visited.add((row,col))
            area = 1
            directions = [(0,-1), (0,1), (-1,0), (1,0)] # left, right, up, down

            while queue:
                for _ in range(len(queue)):
                    curr_row, curr_col = queue.popleft()
					
                    for d_row, d_col in directions:
                        new_row, new_col = curr_row + d_row, curr_col + d_col
                        # check if new row and new col out of bounds
                        if new_row < 0 or new_col < 0 or new_row >= row_len or new_col >= col_len or grid[new_row][new_col] == 0 or (new_row, new_col) in visited:
                            continue # skip new row and new col
                        area += 1
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
            return area
					

        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1 and (row,col) not in visited:
                    max_area = max(max_area, bfs(row,col))
        return max_area
