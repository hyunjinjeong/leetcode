class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # 그룹을 실제로 만드는 문제는 아닌 것 같고..
        # 특정 시점에 겹치는 인터벌의 개수가 그룹 개수네
        # min heap을 쓰면 된다
        intervals.sort(key=lambda tup: tup[0])

        count = 0

        heap = []
        for start, end in intervals:
            while heap and heap[0] < start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            
            count = max(count, len(heap))

        return count
