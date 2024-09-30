class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # greedy하게 못 푸려나?
        # 1개씩 계산을 하면 되려나
        # 그럼 매번 가장 큰 숫자를 뽑아야 함. 그건 heap으로?
        # 뽑고.. 규칙을 만족하면 결과에 더하고 1을 줄여서 다시 넣으면 되고
        # 규칙을 만족하지 않으면? 다음거 뽑고 다시 넣어야 함
        heap = []
        if a:
            heapq.heappush(heap, (-a, "a"))
        if b:
            heapq.heappush(heap, (-b, "b"))
        if c:
            heapq.heappush(heap, (-c, "c"))
        
        res = []
        while heap:
            # 아 heap을 다 돌 필요가 없고.. 2번째까지만 보면 되는구나
            first, char1 = heapq.heappop(heap)
            if len(res) >= 2 and res[-1] == res[-2] == char1:
                if not heap:
                    break
                second, char2 = heapq.heappop(heap)
                res.append(char2)
                if second < -1:
                    heapq.heappush(heap, (second + 1, char2))
            
            res.append(char1)
            if first < -1:
                heapq.heappush(heap, (first + 1, char1))

        return "".join(res)