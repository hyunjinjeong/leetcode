class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # i -> i+1 에서 i의 높이가 i+1과 같거나 크면 아무 것도 안 해도 됨
        # 근데 작은 경우.. 선택을 해야 함. 1. use brick, 2. use ladder
        # brick을 선택한 경우와 ladder를 선택한 경우를 각각 계산해서 max를 구하면 될 것 같은데
        # 그러면 dp

        # @cache
        # def dfs(i, bricks_left, ladders_left):
        #     if bricks_left < 0 or ladders_left < 0:
        #         return 0
        #     if i == len(heights) - 1:
        #         return 1

        #     if heights[i] >= heights[i + 1]:
        #         return 1 + dfs(i + 1, bricks_left, ladders_left)

        #     use_bricks = dfs(i + 1, bricks_left - (heights[i + 1] - heights[i]), ladders_left)
        #     use_ladder = dfs(i + 1, bricks_left, ladders_left - 1)
        #     return 1 + max(use_bricks, use_ladder)
        
        # return dfs(0, bricks, ladders) - 1 # 시작 빌딩은 제외

        # 이거 과정은 맞는데 Memory Limit Exceeded가 뜸. 어떻게 최적화하지
        # Two Pointer? Greedy?
        # Two Pointer는 적용할 방법이 없고.. 힌트를 보니 Greedy에 가깝네
        # ladder는 가장 큰 gap들에 사용해야 함. 그러면 heap을 쓰면 되겠다.
        heap = []
        for i in range(1, len(heights)):
            gap = heights[i] - heights[i - 1]
            if gap <= 0:
                continue
            
            heapq.heappush(heap, gap)
            if len(heap) <= ladders:
                continue
            
            bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i - 1
        
        return len(heights) - 1