class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # 왼쪽 빌딩이 오른쪽 빌딩보다 높이가 낮으면 오른쪽으로 건너갈 수 있음
        # brute force는 query마다 루프를 돌면 되나? 그럼 O(NM)임
        # 대충 monotonic stack 쓰는 문제 같은데..
        def bisect(target):
            lo, hi = 0, len(stack)
            res = -1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if stack[mid][0] > target:
                    res = max(res, mid)
                    lo = mid + 1
                else:
                    hi = mid
            return res

        res = [-1] * len(queries)
        new_queries = [[] for _ in range(len(heights))]

        for i, query in enumerate(queries):
            alice, bob = sorted(query)
            if alice == bob or heights[alice] < heights[bob]:
                res[i] = bob
            else:
                new_queries[bob].append((heights[alice], i))

        stack = []
        for i in range(len(heights) - 1, -1, -1):
            stack_size = len(stack)
            for alice_height, bob in new_queries[i]:
                pos = bisect(alice_height)
                if 0 <= pos < stack_size:
                    res[bob] = stack[pos][1]
            
            while stack and stack[-1][0] <= heights[i]:
                stack.pop()
            
            stack.append((heights[i], i))

        return res
