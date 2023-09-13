class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # # 시간에 따라 갈 수 있는 노드를 정해야 하니까...
        # # time을 어떻게 비교해야 함
        # graph = {i:[] for i in range(1, n + 1)}
        # for u, v, w in times:
        #     graph[u].append((v, w))
        
        # ans = float("inf")
        # q = collections.deque([(k, 0)]) # (node, time)
        # # 노드를 방문한 시각을 dict에 담아두는 게 핵심...
        # visited = {}

        # while q:
        #     node, curr_time_sum = q.popleft()
        #     if node not in visited or curr_time_sum < visited[node]:
        #         visited[node] = curr_time_sum
        #         for next_node, next_time in graph[node]:
        #             q.append((next_node, curr_time_sum + next_time))
          
        # return max(visited.values()) if len(visited) == n else -1
        #
        #
        # 아 최단 경로 거리 구하는 알고리즘들로 해결할 수 있음... 
        # Dijkstra.
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        elapsed_time = [0] + [float("inf")] * n
        heap = [(0, k)]

        while heap:
            time, node = heapq.heappop(heap)
            if time < elapsed_time[node]:
                elapsed_time[node] = time
                for next_node, next_time in graph[node]:
                    heapq.heappush(heap, (time + next_time, next_node))
        
        ans = max(elapsed_time)
        return ans if ans < float("inf") else -1
            