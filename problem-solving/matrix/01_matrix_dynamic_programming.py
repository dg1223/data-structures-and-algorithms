# O(mn) time and space if a separate distance array is returned
# O(mn) time, O(1) space if matrix is modified in-place
# Much faster overall runtime

from collections import deque
import math

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.rows = len(mat)
        self.cols = len(mat[0])   
        self.distance = [row[:] for row in mat]

        # calculate minimum distance iterating from top-left corner
        # compare with top and left cells
        for row, row_element in enumerate(self.distance):
            for col, element in enumerate(row_element):
                # if cell is not 0, then calculate
                if element:
                    top = self.distance[row-1][col] + 1 if row > 0 else math.inf
                    left = self.distance[row][col-1] + 1 if col > 0 else math.inf

                    self.distance[row][col] = min(top, left)

        # calculate minimum distance iterating backwards from bottom-right corner
        # compare with bottom and right cells
        for row, row_element in reversed(list(enumerate(self.distance))):
            for col, element in reversed(list(enumerate(row_element))):
        # for row in range(self.rows-1, -1, -1):
        #     for col in range(self.cols-1, -1, -1):
                # element = self.distance[row][col]
                if element:
                    bottom = self.distance[row+1][col] + 1 if row < self.rows - 1 else math.inf
                    right = self.distance[row][col+1] + 1 if col < self.cols - 1 else math.inf

                    # incorporate the cell's current distance (from above) into comparison
                    self.distance[row][col] = min(element, bottom, right)

        return self.distance