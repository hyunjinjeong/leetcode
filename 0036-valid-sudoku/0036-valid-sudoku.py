class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 각 케이스마다 set을 별도로 만들면 1-pass에 해결 가능하넹
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        sub_box_set = [[set() for _ in range(3)] for _ in range(3)]
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                
                if num in row_set[r] or num in col_set[c] or num in sub_box_set[r//3][c//3]:
                    return False
                
                row_set[r].add(num)
                col_set[c].add(num)
                sub_box_set[r//3][c//3].add(num)
        
        return True