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
            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            # 더 이상 범위가 없는 아이템은 뺌
            while intervals and intervals[-1][0] <= query:
                left, right = intervals.pop()
                if right >= query:
                    size = right - left + 1
                    heapq.heappush(heap, (size, right))
            
            # while heap and heap[0][1] < query:
            #     heapq.heappop(heap)
            
            if heap:
                size, _ = heap[0]
                min_sizes[query] = size

        return [min_sizes.get(query, -1) for query in queries]