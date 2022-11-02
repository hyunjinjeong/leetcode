class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c):
            if r < 0 or r >= len(image):
                return
            if c < 0 or c >= len(image[0]):
                return
            if image[r][c] != original_color:
                return
            
            image[r][c] = color
            for move in moves:
                dfs(r+move[0], c+move[1])
            
        dfs(sr, sc)
        return image