class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # 단순하게 dict에 모든 숫자에 대한 최솟값을 저장하면 됨
        # 다만 이 경우 시간 및 메모리가 너무 큼.
        # 최적화할 방법이 있을까?
        # 정렬한 후에 heap을 이용하는 방법이 있다..
        intervals.sort()

        min_sizes = {}
        heap = []
        i = 0 # intervals index

        for query in sorted(set(queries)): # 같은 수는 다 결과가 같으니...
            while i < len(intervals) and intervals[i][0] <= query: # left <= query
                left, right = intervals[i]
                size = right - left + 1
                heapq.heappush(heap, (size, right))
                i += 1

            # 더 이상 범위가 없는 경우는 heap에서 뺌. right < query
            # size의 최솟값이 유효하기만 하면 되기 때문에 head만 체크. lazy하게 제거하는 것
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            min_sizes[query] = heap[0][0] if heap else -1

        return [min_sizes[query] for query in queries]