class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # heap을 사용하면..
        # 스케줄된 task index를 t_i라고 했을 때
        # heap에다가 t_i를 넣고
        # 현재 i - n > t_i 인지를 검사하면 되려나?
        # 아 이렇게하면 안 되는게 가장 갯수가 많은 task를 최대한 빨리 줄여야 함.
        # greedy. n개씩 사이클을 돌려야 함

        ans = 0
        heap = []
        
        counter = Counter(tasks)
        for freq in counter.values():
            heapq.heappush(heap, freq * -1) # freq가 높은 task가 우선 순위가 높도록
        
        while heap:
            temp = []
            for _ in range(n+1):
                ans += 1
                if heap:
                    negative_freq = heapq.heappop(heap)
                    if negative_freq < -1:
                        temp.append(negative_freq + 1) # negative니까 +1

                if not heap and not temp:
                    break
            
            for negative_freq in temp:
                heapq.heappush(heap, negative_freq)
        
        return ans