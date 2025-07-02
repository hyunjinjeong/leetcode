class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # brute force는 grid를 다 순회해서 찾으면 됨
        # 근데 hard인거 보면 최적화가 가능한가본데
        # 쿼리를 오름차순으로 정렬하면 이전 결과를 재활용할 수 있나?
        # 오.. pq를 쓰는 거였음
        M, N = len(grid), len(grid[0])

        res = [0 for _ in range(len(queries))]
        sorted_queries = sorted([(query, i) for i, query in enumerate(queries)])

        heap = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        count = 0
        
        for query, original_index in sorted_queries:
            while heap and heap[0][0] < query:
                val, x, y = heapq.heappop(heap)
                count += 1
                
                for next_x, next_y in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                    if 0 <= next_x < M and 0 <= next_y < N and (next_x, next_y) not in visited:
                        heapq.heappush(heap, (grid[next_x][next_y], next_x, next_y))
                        visited.add((next_x, next_y))

            res[original_index] = count

        return res
