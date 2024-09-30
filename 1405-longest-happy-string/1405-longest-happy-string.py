class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # greedy하게 못 푸려나?
        # abc 돌아가면서 2개씩 넣고.. prev가 curr랑 동일하면 skip하고
        # 남은 갯수가 1이면 1 넣고.. 뭐 이런 식으로?
        # 근데 abc 순서대로 하면 a = 1, b = 7 이런 경우 abb 요렇게 됨
        # 그러면 순서를 갯수가 큰 순서대로 넣으면?
        # 흠 근데 꼭 2개씩 넣는게 답은 아닐거 같은데
        # a = 2, b = 0, c = 7이라고 할 때
        # ccaacc 보다는
        # ccaccacc 이게 더 기니까...
        # a = 7, b = 7이라고 하면 걍 14짜리가 되고
        # 그러면 가장 긴 것도 2개씩 넣는게 아닌데..
        # 1개씩 계산을 하면 되려나
        # 그럼 매번 가장 큰 숫자를 뽑아야 함. 그건 heap으로?
        # 뽑고.. 규칙을 만족하면 결과에 더하고 1을 줄여서 다시 넣으면 되고
        # 규칙을 만족하지 않으면? 다음거 뽑고 다시 넣어야 함
        heap = [(-a, "a"), (-b, "b"), (-c, "c")]
        heapq.heapify(heap)
        res = []
        
        while heap:
            tmp = []
            char_used = False
            while heap:
                limit, char = heapq.heappop(heap)
                if limit == 0:
                    continue
                if len(res) < 2 or not (res[-1] == res[-2] == char):
                    res.append(char)
                    char_used = True
                    if limit < -1:
                        tmp.append((limit + 1, char))
                    break
                else:
                    tmp.append((limit, char))
            
            if not char_used:
                break
            
            for item in tmp:
                heapq.heappush(heap, item)

        return "".join(res)