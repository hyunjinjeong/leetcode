class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # 괴물마다 걸리는 시간을 구해서
        # greedy로 풀기?
        times = []
        for i in range(len(dist)):
            times.append(math.ceil(dist[i] / speed[i]))
        heapq.heapify(times)

        heapq.heappop(times) # 0초에 하나 죽일 수 있음
        res = 1

        curr_time = 1
        while times:
            time = heapq.heappop(times)
            if curr_time >= time:
                break
            curr_time += 1
            res += 1
        
        return res