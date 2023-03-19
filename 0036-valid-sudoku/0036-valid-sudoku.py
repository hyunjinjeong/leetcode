class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 이것도 일단 brute force로 구현해보자.
        
        # 1. Each row must contain the digits 1-9 without repetition.
        def check_rows():
            for r in range(9):
                s = set()
                for c in range(9):
                    num = board[r][c]
                    if num == ".":
                        continue
                    if num in s:
                        return False
                    s.add(num)
            return True
        
        # 2. Each column must contain the digits 1-9 without repetition.
        def check_columns():
            for c in range(9):
                s = set()
                for r in range(9):
                    num = board[r][c]
                    if num == ".":
                        continue
                    if num in s:
                        return False
                    s.add(num)
            return True
        
        # 3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        def check_sub_boxes(row_start, col_start):
            s = set()
            for r in range(row_start, row_start+3):
                for c in range(col_start, col_start+3):
                    num = board[r][c]
                    if num == ".":
                        continue
                    if num in s:
                        return False
                    s.add(num)
            return True
        
        return check_rows() and check_columns() and check_sub_boxes(0, 0) and check_sub_boxes(0, 3) and check_sub_boxes(0, 6) and check_sub_boxes(3, 0) and check_sub_boxes(3, 3) and check_sub_boxes(3, 6) and check_sub_boxes(6, 0) and check_sub_boxes(6, 3) and check_sub_boxes(6, 6)