class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.rows = len(grid2)
        self.cols = len(grid2[0])
        self.visited = [ [False] * self.cols for _ in range(self.rows) ]
        self.DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.grid1 = grid1
        self.grid2 = grid2

        num_sub_islands = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.visited[row][col] and self.grid2[row][col] == 1:
                    self.common_land = True
                    self.dfs(row, col)
                    if self.common_land:
                        num_sub_islands += 1

        return num_sub_islands

    def dfs(self, source_i, source_j):
        self.visited[source_i][source_j] = True
        if self.grid1[source_i][source_j] != self.grid2[source_i][source_j]:
            self.common_land = False

        for direction in self.DIRECTIONS:
            child_i = source_i + direction[0]
            child_j = source_j + direction[1]

            if self.is_valid(child_i, child_j) and not self.visited[child_i][child_j] and self.grid2[child_i][child_j] == 1:
                self.dfs(child_i, child_j)

    def is_valid(self, child_i, child_j):
        return child_i >= 0 and child_i < self.rows and child_j >= 0 and child_j < self.cols