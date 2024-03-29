class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # backtracking..?
        # 근데 너무 경우의 수가 많지 않나... 9*9라서 괜찮은 건가
        # 한 점 board[x][y]에서 row, column, sub-box를 검사해서 가능한 수를 넣고
        # 안되면 backtrack..?
        
#         def check_row(row, num):
#             for col in range(9):
#                 if board[row][col] == num:
#                     return False
#             return True
        
#         def check_col(col, num):
#             for row in range(9):
#                 if board[row][col] == num:
#                     return False
#             return True
        
#         def check_square(r, c, num):
#             start_r, start_c = r - r%3, c - c%3
#             for row in range(start_r, start_r+3):
#                 for col in range(start_c, start_c+3):
#                     if board[row][col] == num:
#                         return False
#             return True
        
        # def is_valid(r, c, num):
        #     return check_row(r, num) and check_col(c, num) and check_square(r, c, num)
        
        def add_sets(r, c, num):
            row_set.add((r, num))
            col_set.add((c, num))
            square_set.add((r//3, c//3, num))
        
        def remove_sets(r, c, num):
            row_set.remove((r, num))
            col_set.remove((c, num))
            square_set.remove((r//3, c//3, num))
        
        def is_valid(r, c, num):
            if (r, num) in row_set:
                return False
            if (c, num) in col_set:
                return False
            if (r//3, c//3, num) in square_set:
                return False
            return True
        
        def solve(r, c):
            if r == 9: # 모든 케이스를 다 돈 경우
                return True 
            if c == 9: # 열 다 돈 경우
                return solve(r + 1, 0)
            if board[r][c] != ".": # 숫자면 그냥 지나가고...
                return solve(r, c + 1)
            
            for num in range(1, 10):
                str_num = str(num)
                if not is_valid(r, c, str_num):
                    continue
                
                board[r][c] = str_num
                add_sets(r, c, str_num)
                if solve(r, c+1):
                    return True
                board[r][c] = "." # backtrack
                remove_sets(r, c, str_num)
            
            return False
        
        # is_valid를 좀 더 효율적으로. set을 활용해보자
        row_set, col_set, square_set = set(), set(), set()
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                add_sets(r, c, num)
        
        solve(0, 0)