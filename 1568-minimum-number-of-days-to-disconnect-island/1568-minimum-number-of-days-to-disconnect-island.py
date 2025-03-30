class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # island가 하나만 있을 때가 connected. 그러면 2개로만 쪼개면 disconnected임
        # 처음부터 disconnected일 수도 있다. 1의 개수를 세서 모두 연결되어 있는지 확인하면 됨
        # connected grid를 disconnect 시키려면? 일단 max가 2인데? 모서리에 2개 떼어내면 됨.
        M, N = len(grid), len(grid[0])

        def get_one_count(i, j, visited):
            count = 1

            visited.add((i, j))
            for adj_i, adj_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= adj_i < M and 0 <= adj_j < N and grid[adj_i][adj_j] == 1 and (adj_i, adj_j) not in visited:
                    count += get_one_count(adj_i, adj_j, visited)

            return count

        one_count = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    one_count += 1
        
        if one_count == 0:
            return 0
        if one_count == 1:
            return 1

        entered = False
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    if get_one_count(i, j, set()) != one_count:
                        return 0
                    entered = True
                    break
            if entered:
                break
        
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    for adj_i, adj_j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= adj_i < M and 0 <= adj_j < N and grid[adj_i][adj_j] == 1:
                            if get_one_count(adj_i, adj_j, set()) < one_count - 1:
                                return 1
                    grid[i][j] = 1
        
        return 2