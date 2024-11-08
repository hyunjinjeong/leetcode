class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # DP나 backtracking 같이 생겼네
        N = len(board)

        def coordinates(num):
            length = N - 1
            index = num - 1
            quotient, remainder = divmod(index, N)

            row = length - quotient
            col = remainder if quotient % 2 == 0 else length - remainder
            return (row, col)

        # 뭔가 BFS가 더 편한 듯
        visited = set()

        q = collections.deque([(1, 0)])
        while q:
            for _ in range(len(q)):
                curr, count = q.popleft()
                if curr == N ** 2:
                    return count
                
                for next_cell in range(curr + 1, min(curr + 6, N ** 2) + 1):
                    if next_cell in visited:
                        continue
                    
                    r, c = coordinates(next_cell)
                    if board[r][c] != -1:
                        q.append((board[r][c], count + 1))
                    else:
                        q.append((next_cell, count + 1))
                    
                    visited.add(next_cell)
        
        return -1