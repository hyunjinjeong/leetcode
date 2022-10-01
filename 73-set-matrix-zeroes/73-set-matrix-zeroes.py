class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
#         # 일단 naive 하게 가보자
#         len_row, len_col = len(matrix), len(matrix[0])
#         zero_rows, zero_cols = [False] * len_row, [False] * len_col
        
#         # 0 있으면 체크
#         for r in range(len_row):
#             for c in range(len_col):
#                 if matrix[r][c] == 0:
#                     zero_rows[r] = True
#                     zero_cols[c] = True
        
#         # True로 찍힌 애들은 다 0으로 만들어 줌
#         for r in range(len_row):
#             for c in range(len_col):
#                 if zero_rows[r] or zero_cols[c]:
#                     matrix[r][c] = 0

        # follow-up으로 공간 복잡도를 O(1)로 만들어야 함!
        # 어디선가 본 풀이인데... 0번째 row, col에 0이 있는지 체크하는 변수만 만들고
        # 0번째 row, col을 위의 zero_rows, zero_cols 용도로 쓰면 될 듯?
        len_row, len_col = len(matrix), len(matrix[0])
        
        is_first_row_zero, is_first_col_zero = False, False
        for c in range(len_col):
            if matrix[0][c] == 0:
                is_first_row_zero = True
        for r in range(len_row):
            if matrix[r][0] == 0:
                is_first_col_zero = True
        
        # 다음으로 0 있으면 체크
        for r in range(len_row):
            for c in range(len_col):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # 0번째 col, row 보면서 0이 있으면 0으로 덮어써줌.
        # index가 1부터 시작하는 이유는 0번째로하면 덮어써져버림.
        for c in range(1, len_col):
            if matrix[0][c] == 0:
                for r in range(1, len_row):
                    matrix[r][c] = 0
        for r in range(1, len_row):
            if matrix[r][0] == 0:
                for c in range(1, len_col):
                    matrix[r][c] = 0
        
        # 0번째 row, col도 처리
        if is_first_row_zero:
            for c in range(len_col):
                matrix[0][c] = 0
        if is_first_col_zero:
            for r in range(len_row):
                matrix[r][0] = 0