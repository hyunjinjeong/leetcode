class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        M, N = len(image), len(image[0])
        
        def dfs(r, c):
            original_color = image[r][c]
            if original_color == color:
                return
            
            image[r][c] = color

            for adj_r, adj_c in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if 0 <= adj_r < M and 0 <= adj_c < N and image[adj_r][adj_c] == original_color:
                    dfs(adj_r, adj_c)
        
        dfs(sr, sc)
        return image
