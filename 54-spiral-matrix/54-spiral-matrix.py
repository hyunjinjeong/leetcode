class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 요것도 naive 하게 먼저 가보자
        visited = set()
        
        total_counts = len(matrix) * len(matrix[0])
        # R, D, L, U 순서대로 시도.
        moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        answer = []
        
        r, c = 0, 0
        curr_direction = 0
        while len(answer) < total_counts:
            # 회전해야 하는 조건들. range 벗어났거나 이미 방문한 경우
            if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or (r, c) in visited:
                move = moves[curr_direction]
                before_r, before_c = r - move[0], c - move[1]
                
                curr_direction = (curr_direction + 1) % 4
                move = moves[curr_direction]
                r, c = before_r + move[0], before_c + move[1]
                continue
            
            answer.append(matrix[r][c])
            visited.add((r, c))
            
            move = moves[curr_direction]
            r, c = r + move[0], c + move[1]
            
        return answer