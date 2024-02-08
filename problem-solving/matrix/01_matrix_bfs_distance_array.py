from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.rows = len(mat)
        self.cols = len(mat[0])
        self.DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.visited = [ [False] * self.cols for _ in range(self.rows) ]        
        self.distance = [row[:] for row in mat]

        queue = deque()

        # Mark all cells with distance 0 as visited and enqueue them
        for row in range(self.rows):
            for col in range(self.cols):
                if self.distance[row][col] == 0:
                    queue.appendleft((row, col))
                    self.visited[row][col] = True

        while queue:
            parent_i, parent_j = queue.pop()

            for direction in self.DIRECTIONS:
                child_i = parent_i + direction[0]
                child_j = parent_j + direction[1]

                # skip cells with distance 0 because their distances won't change
                # also skip out of bound cells
                if not self.is_valid(child_i, child_j) or self.visited[child_i][child_j]:
                    continue

                # if cell hasn't been visited yet, then it is not 0. Update its disance
                queue.appendleft((child_i, child_j))
                self.visited[child_i][child_j] = True
                self.distance[child_i][child_j] = self.distance[parent_i][parent_j] + 1

        return self.distance
                
    # check corners and edges
    def is_valid(self, child_i, child_j):
        return child_i >= 0 and child_i < self.rows and child_j >= 0 and child_j < self.cols