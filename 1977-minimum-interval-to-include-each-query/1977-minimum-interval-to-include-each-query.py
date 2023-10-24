class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # 단순하게 dict에 모든 숫자에 대한 최솟값을 저장하면 됨
        # 다만 이 경우 시간 및 메모리가 너무 큼.
        # 최적화할 방법이 있을까?
        # 정렬한 후에 heap을 이용하는 방법이 있다..
        intervals.sort(reverse=True) # pop()을 O(1)로 하기 위해 거꾸로

        min_sizes = {}
        heap = []

        for query in sorted(set(queries)): # 같은 수는 다 결과가 같으니...
            # 더 이상 범위가 없는 경우는 heap에서 뺌. right < query
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            while intervals and intervals[-1][0] <= query: # left <= query
                left, right = intervals.pop()
                # query가 정렬되어 있으니까 이 경우에만 넣으면 됨. right < query이면 해당 interval에 포함되는 query가 없는 것
                if right >= query:
                    size = right - left + 1
                    heapq.heappush(heap, (size, right))
            
            if heap:
                size, _ = heap[0]
                min_sizes[query] = size

        return [min_sizes.get(query, -1) for query in queries]