class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = collections.deque()
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    # 0인거부터 시작하기 위해 넣고
                    q.append((r, c))
                else:
                    # 방문했는지 안헀는지 표시하기 위해 -1로 초기화. 별도의 visited set을 안 가져감.
                    mat[r][c] = -1
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # BFS 돌리기
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                
                # 범위 벗어난 경우들
                if not (0 <= new_r < len(mat)):
                    continue
                if not (0 <= new_c < len(mat[0])):
                    continue
                
                # 이미 방문한 경우
                if mat[new_r][new_c] != -1:
                    continue
                
                mat[new_r][new_c] = mat[r][c] + 1
                q.append((new_r, new_c))
                
        return mat
        
        
        