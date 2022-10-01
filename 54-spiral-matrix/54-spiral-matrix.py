class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 요것도 naive 하게 먼저 가보자
        visited = set()
        
        total_count = len(matrix) * len(matrix[0])
        # R, D, L, U 순서대로 시도.
        moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        r, c = 0, 0
        curr_direction = 0
        answer = [matrix[r][c]]
        visited.add((r, c))
        while len(answer) < total_count:
            move = moves[curr_direction]
            next_r, next_c = r + move[0], c + move[1]
            
            # matrix 안에 있고 방문하지 않은 경우. 그대로 가면 됨
            if 0 <= next_r < len(matrix) and 0 <= next_c < len(matrix[0]) and (next_r, next_c) not in visited:
                answer.append(matrix[next_r][next_c])
                visited.add((next_r, next_c))
                r, c = next_r, next_c
            # 조건에 안 맞으면 회전해야 됨
            else:
                curr_direction = (curr_direction + 1) % 4
            
        return answer