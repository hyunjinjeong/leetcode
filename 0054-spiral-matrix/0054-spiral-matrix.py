class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        res = []

        x, y, dx, dy = 0, 0, 0, 1
        for _ in range(M * N):
            res.append(matrix[x][y])
            matrix[x][y] = "-"
            
            if not 0 <= x + dx < M or not 0 <= y + dy < N or matrix[x + dx][y + dy] == "-":
                dx, dy = dy, -dx

            x, y = x + dx, y + dy
        
        return res