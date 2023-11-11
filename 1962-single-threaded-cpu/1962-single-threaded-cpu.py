class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # 일단 시간에 따라서.. 어떤 task들이 가능한지 알아야 하고
        # 또 shortest processing time을 가진 task를 알아야 함
        # 그러면 heap을 쓰면?
        # enqueuetime으로 정렬한 다음에
        # 현재 가능한 task 집합이 있을 거고.. 그건 heap에 넣어서 하나씩 뽑기
        # (enqueueTime, processingTime, index)으로 정렬해서 heap에는 (processingTime, index)로.

        # enqueueTime, processingTime, originalIndex
        sorted_tasks = sorted([(task[0], task[1], i) for i, task in enumerate(tasks)])
        heap = []
        
        ans = []
        print(sorted_tasks)
        i = 0
        curr_time = sorted_tasks[0][0]
        while len(ans) < len(tasks):
            # curr_time보다 <= 인 task 다 넣기
            while i < len(tasks) and sorted_tasks[i][0] <= curr_time:
                # processingTime, original_index
                heapq.heappush(heap, (sorted_tasks[i][1], sorted_tasks[i][2]))
                i += 1
            
            # heap에서 꺼내서 처리하기
            if heap:
                processing_time, original_index = heapq.heappop(heap)
                curr_time += processing_time
                ans.append(original_index)
            elif i < len(tasks): # 중간에 시간이 빈 경우.
                curr_time = sorted_tasks[i][0]
        
        return ans