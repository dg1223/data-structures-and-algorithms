class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_pixel_color = image[sr][sc]
        dim = [len(image), len(image[sr])]

        self.dfs(image, sr, sc, color, starting_pixel_color, dim)

        return image

    def dfs(self, image, sr, sc, color, starting_pixel_color, dim):
        row, col = dim
        
        if  sr < 0 or sc < 0:
            return None
        if sr > row - 1 or sc > col - 1:
            return None
        if starting_pixel_color == color or image[sr][sc] != starting_pixel_color:
            return None

        image[sr][sc] = color
        
        self.dfs(image, sr+1, sc, color, starting_pixel_color, dim)
        self.dfs(image, sr-1, sc, color, starting_pixel_color, dim)
        self.dfs(image, sr, sc-1, color, starting_pixel_color, dim)
        self.dfs(image, sr, sc+1, color, starting_pixel_color, dim)