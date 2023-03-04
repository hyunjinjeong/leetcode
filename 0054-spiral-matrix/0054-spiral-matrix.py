class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         # 요것도 naive 하게 먼저 가보자
#         total_count = len(matrix) * len(matrix[0])
#         # R, D, L, U 순서대로 시도.
#         moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
#         r, c = 0, -1
#         curr_direction = 0
#         answer = []
#         while len(answer) < total_count:
#             move = moves[curr_direction]
#             next_r, next_c = r + move[0], c + move[1]
            
#             # matrix 안에 있고 방문하지 않은 경우. 그대로 가면 됨
#             if 0 <= next_r < len(matrix) and 0 <= next_c < len(matrix[0]) and matrix[next_r][next_c] != "":
#                 answer.append(matrix[next_r][next_c])
#                 matrix[next_r][next_c] = ""
#                 r, c = next_r, next_c
#             # 조건에 안 맞으면 회전해야 됨
#             else:
#                 curr_direction = (curr_direction + 1) % 4
            
#         return answer
        # 내가 푼건 이건데... 더 간단하게 가능했음. 걍 바운더리들마다 변수 지정해서 돌면 된다.
        RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
        answer = []
        
        row_begin, col_begin = 0, 0
        row_end, col_end = len(matrix)-1, len(matrix[0])-1
        direction = 0
        
        while row_begin <= row_end and col_begin <= col_end:
            if direction == RIGHT:
                for col in range(col_begin, col_end+1):
                    answer.append(matrix[row_begin][col])
                row_begin += 1
            elif direction == DOWN:
                for row in range(row_begin, row_end+1):
                    answer.append(matrix[row][col_end])
                col_end -= 1
            elif direction == LEFT:
                for col in range(col_end, col_begin-1, -1):
                    answer.append(matrix[row_end][col])
                row_end -= 1
            elif direction == UP:
                for row in range(row_end, row_begin-1, -1):
                    answer.append(matrix[row][col_begin])
                col_begin += 1
            
            direction = (direction + 1) % 4
        
        return answer