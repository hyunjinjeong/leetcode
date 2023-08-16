class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # heap을 사용하면..
        # 스케줄된 task index를 t_i라고 했을 때
        # heap에다가는 freq만 넣고 queue를 이용해서 조건이 만족하면 heap에 넣어줄 수 있음
        counter = Counter(tasks)
        max_heap = [-1 * count for count in counter.values()]
        heapq.heapify(max_heap)
        
        time = 0
        q = collections.deque() # (count, idle_time)
        while max_heap or q:
            time += 1

            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count < 0:
                    q.append((count, time + n))
            
            if q and q[0][1] == time:
                count = q.popleft()[0]
                heapq.heappush(max_heap, count)
        
        return time