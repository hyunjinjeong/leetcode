class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # heap을 쓸 수 있을 것 같은디. weight, index로 해서.
        # 문제는 빼고 난 다음에 어떻게 다시 넣을 것인가..? 
        # 아..! 사용 못하는 서버도 heap으로 관리하면 됨. 이건 time을 넣으면 될 것 같음. (i초면 time이 i인걸 모두 빼서 다시 heap으로 넣으면 됨)
        ans = []
        available, unavailable = [], []

        for index, weight in enumerate(servers):
            heapq.heappush(available, (weight, index))
        
        # time과 task에 대한 index는 따로 관리해야겠지?
        # 빈 서버가 없으면 기다려야 한다고 했으니까..
        time = 0
        task_index = 0
        while task_index < len(tasks):
            # 먼저 작업 끝난 서버를 다시 available에 넣어 주고...
            while unavailable and unavailable[0][0] <= time:
                _, server_index = heapq.heappop(unavailable)
                heapq.heappush(available, (servers[server_index], server_index))

            # 이제 로직은 맞는데 TLE가 뜬다.
            # 뭘 하면 최적화할 수 있을라나
            # 위는 필수인 것 같고 여기 밑으로 고쳐야 할 것 같은데

            # 현재 시간까지의 task만 큐에 들어가 있으니까...
            while available and task_index < len(tasks) and task_index <= time:
                _, server_index = heapq.heappop(available)
                heapq.heappush(unavailable, (time + tasks[task_index], server_index))

                ans.append(server_index)
                task_index += 1
            
            if not available:
                time = unavailable[0][0]
            else:
                time += 1

        return ans