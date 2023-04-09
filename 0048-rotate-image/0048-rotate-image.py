class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
#         # nxn 매트릭스니까 정사각형임.
#         # 대략 아래같은 로직일텐데...
#         # row[i] -> col[len-1-i]
#         # col[len-1-i] -> row[len-1-i]
#         # row[len-1-i] -> col[i]
#         # col[i] -> row[i]
#         # row, col 단위가 아니라 cell 단위로 하는 것!
#         len_mat = len(matrix)
#         layer = 0
        
#         while layer * 2 < len_mat:
#             first, last = 0 + layer, len_mat - layer - 1
#             for i in range(first, last):
#                 offset = i - first
#                 tmp_top = matrix[first][i]
#                 # left -> top
#                 matrix[first][i] = matrix[last-offset][first]
#                 # bottom -> left
#                 matrix[last-offset][first] = matrix[last][last-offset]
#                 # right -> bottom
#                 matrix[last][last-offset] = matrix[i][last]
#                 # top -> right
#                 matrix[i][last] = tmp_top
#             layer += 1

        # math 이용하면 위아래로 reverse하고 transpose 하면 됨...
        # 90도는 row reverse + transpose
        # 180: Reverse Rows + Reverse columns
        # 270(혹은 -90도)는 col reverse + transpose
        start, end = 0, len(matrix) - 1
        # 1. reverse rows
        while start < end:
            matrix[start], matrix[end] = matrix[end], matrix[start]
            start += 1
            end -= 1
        # 2. transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]