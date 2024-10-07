class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # prefix sum을 활용해야 할 것 같은데..
        # row 단위, col 단위로 각각 저장할까?
        # 아.. grid 하나하나씩 보는게 아니라 rectangle 단위로 저장하는구나. 0부터 해당 포인트까지...
        M, N = len(matrix), len(matrix[0])        
        self.prefix_sum = [[0] * N for _ in range(M)]

        for r in range(M):
            for c in range(N):
                upper = self.prefix_sum[r - 1][c] if r > 0 else 0
                left = self.prefix_sum[r][c - 1] if c > 0 else 0
                upper_left = self.prefix_sum[r - 1][c - 1] if r > 0 and c > 0 else 0

                self.prefix_sum[r][c] = matrix[r][c] + upper + left - upper_left

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        upper = self.prefix_sum[row1 - 1][col2] if row1 > 0 else 0
        left = self.prefix_sum[row2][col1 - 1] if col1 > 0 else 0
        upper_left = self.prefix_sum[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0

        return self.prefix_sum[row2][col2] - upper - left + upper_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)