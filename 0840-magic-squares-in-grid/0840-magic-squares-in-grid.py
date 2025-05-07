class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        # row, col이 최대 10개씩이니까 그냥 쭉 돌면서 다 체크해도 되지 않나?
        # 그렇게 하고 최적화할 여지를 찾아보자
        def is_magic_square(row, col):
            

            # distinct
            numbers = set()
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    num = grid[r][c]
                    if num in numbers:
                        return False
                    if not 1 <= num <= 9:
                        return False
                    numbers.add(num)
            
            # rows
            target_sum = None
            for r in range(row, row + 3):
                curr_sum = grid[r][col] + grid[r][col+1] + grid[r][col+2]
                if target_sum is None:
                    target_sum = curr_sum
                elif target_sum != curr_sum:
                    return False
            
            # cols
            for c in range(col, col + 3):
                curr_sum = grid[row][c] + grid[row+1][c] + grid[row+2][c]
                if target_sum != curr_sum:
                    return False

            # diagonals
            top_left = grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2]
            if top_left != target_sum:
                return False
            top_right = grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col]
            if top_right != target_sum:
                return False
            
            return True
        
        count = 0
        for row in range(ROW - 2):
            for col in range(COL - 2):
                if is_magic_square(row, col):
                    count += 1
        return count
