class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # heap을 쓸 수 있을 것 같은디. weight, index로 해서.
        # 문제는 빼고 난 다음에 어떻게 다시 넣을 것인가..? 
        # 아..! 사용 못하는 서버도 heap으로 관리하면 됨. 이건 time을 넣으면 될 것 같음. (i초면 time이 i인걸 모두 빼서 다시 heap으로 넣으면 됨)
        ans = []
        available, unavailable = [], []

        for index, weight in enumerate(servers):
            available.append((weight, index))
        heapq.heapify(available)
        
        time = 0
        # time을 기준으로 while 문을 돌릴 필요가 없었구나
        for i, process_time in enumerate(tasks):
            time = max(i, time)
            if not available:
                time = unavailable[0][0]
            
            # 먼저 작업 끝난 서버를 다시 available에 넣어 주고...
            while unavailable and unavailable[0][0] <= time:
                _, server_index = heapq.heappop(unavailable)
                heapq.heappush(available, (servers[server_index], server_index))
            
            # 작업 할당
            _, server_index = heapq.heappop(available)
            heapq.heappush(unavailable, (time + process_time, server_index))
            
            ans.append(server_index)

        return ans