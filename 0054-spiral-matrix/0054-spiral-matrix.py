class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
        ans = []

        first_row, first_col = 0, 0
        last_row, last_col = M - 1, N - 1
        direction = 0

        while first_row <= last_row and first_col <= last_col:
            if direction == RIGHT:
                for col in range(first_col, last_col + 1):
                    ans.append(matrix[first_row][col])
                first_row += 1
            elif direction == DOWN:
                for row in range(first_row, last_row + 1):
                    ans.append(matrix[row][last_col])
                last_col -= 1
            elif direction == LEFT:
                for col in range(last_col, first_col - 1, -1):
                    ans.append(matrix[last_row][col])
                last_row -= 1
            else:
                for row in range(last_row, first_row - 1, -1):
                    ans.append(matrix[row][first_col])
                first_col += 1

            direction = (direction + 1) % 4
        
        return ans