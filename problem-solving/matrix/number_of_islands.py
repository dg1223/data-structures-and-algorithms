class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = [ [False] * self.cols for _ in range(self.rows) ]
        self.DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.grid = grid

        num_islands = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.visited[row][col] and self.grid[row][col] == '1':
                    self.dfs(row, col)
                    num_islands += 1

        return num_islands

    def dfs(self, source_i, source_j):
        self.visited[source_i][source_j] = True
        
        for direction in self.DIRECTIONS:
            child_i = source_i + direction[0]
            child_j = source_j + direction[1]

            if self.is_valid(child_i, child_j) \
                and not self.visited[child_i][child_j] \
                and self.grid[child_i][child_j] == '1':
                self.dfs(child_i, child_j)

    def is_valid(self, child_i, child_j):
        return child_i >= 0 and child_i < self.rows and child_j >= 0 and child_j < self.cols