class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # 이거는 그냥 돌면 될 것 같은디
        # 근데 m이랑 n이 커서 그건 아닌가.. 아니면 어케 풂?
        # 일단 ㄱㄱ
        def check_guarded_cells(r, c):
            # up
            for adj_r in range(r - 1, -1, -1):
                if matrix[adj_r][c] > 0:
                    break
                matrix[adj_r][c] = -1
            # down
            for adj_r in range(r + 1, m):
                if matrix[adj_r][c] > 0:
                    break
                matrix[adj_r][c] = -1
            # right
            for adj_c in range(c + 1, n):
                if matrix[r][adj_c] > 0:
                    break
                matrix[r][adj_c] = -1
            # left
            for adj_c in range(c - 1, -1, -1):
                if matrix[r][adj_c] > 0:
                    break
                matrix[r][adj_c] = -1


        matrix = [[0] * n for _ in range(m)]

        for r, c in guards:
            matrix[r][c] = 1
        for r, c in walls:
            matrix[r][c] = 2
        
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 1:
                    check_guarded_cells(r, c)
        
        count = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    count += 1
        
        return count
