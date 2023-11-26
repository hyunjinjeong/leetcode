class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 기본적으로 1개. 특정 시간대에 겹치는 인터벌 개수만큼 늘어남.
        # heap 쓰면 될 듯?
        START, END = 0, 1
        
        ans = 1
        intervals.sort()
        heap = [intervals[0][END]]
        
        for i in range(1, len(intervals)):
            if heap[0] <= intervals[i][START]:
                heapq.heappop(heap)
            
            heapq.heappush(heap, intervals[i][END])
        
        return len(heap)