class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # 왼쪽 빌딩이 오른쪽 빌딩보다 높이가 낮으면 오른쪽으로 건너갈 수 있음
        # brute force는 query마다 루프를 돌면 되나? 그럼 O(NM)임
        # 대충 monotonic stack 쓰는 문제 같은데..
        # def bisect(target):
        #     lo, hi = 0, len(stack)
        #     while lo < hi:
        #         mid = lo + (hi - lo) // 2
        #         if heights[stack[mid]] > target:
        #             lo = mid + 1
        #         else:
        #             hi = mid
        #     return lo - 1 # lo is the first index that satifies <= target. So lo - 1 is the last index for > target.

        res = [-1] * len(queries)
        new_queries = [[] for _ in range(len(heights))]

        for i, query in enumerate(queries):
            alice, bob = sorted(query)
            if alice == bob or heights[alice] < heights[bob]:
                res[i] = bob
            else: # heights[alice] > heights[bob]
                new_queries[bob].append((heights[alice], i))

        # stack = [] # monotonically decreasing
        # for bob in range(len(heights) - 1, -1, -1):
        #     for alice_height, query_index in new_queries[bob]:
        #         pos = bisect(alice_height) # the smallest index which has heights[index] > alice_height
        #         if 0 <= pos < len(stack):
        #             res[query_index] = stack[pos]
            
        #     while stack and heights[stack[-1]] <= heights[bob]:
        #         stack.pop()
            
        #     stack.append(bob)

        # min heap을 쓸 수도 있다. 이 경우엔 오름차순
        heap = []
        for bob in range(len(heights)):
            while heap and heap[0][0] < heights[bob]:
                alice_height, query_index = heapq.heappop(heap)
                res[query_index] = bob
            
            for alice_height, query_index in new_queries[bob]:
                heapq.heappush(heap, (alice_height, query_index))

        return res
