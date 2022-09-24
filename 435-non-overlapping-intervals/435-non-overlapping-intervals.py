class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         START, END = 0, 1
#         # 여기도 interval 순서는 뒤죽박죽...
#         intervals.sort(key=lambda interval: interval[START])
        
#         last_end = float("-inf")
#         answer = 0
#         for interval in intervals:
#             # last_end가 갱신되어야 하는 경우
#             if last_end > interval[START]:
#                 # last_end가 갱신되는 경우.
#                 answer += 1
#                 # END가 더 큰거를 없애야 함. 뒤에 영향이 안 가게..
#                 last_end = min(last_end, interval[END])
#             else:
#                 # 겹치지 않는 경우엔 아니면 last_end를 업데이트해준다.
#                 last_end = interval[END]
                
#         return answer
    
        # end time으로 정렬하면 더 간단한 greedy가 됨. end가 큰 것만 greedy하게 없애는 것..
        START, END = 0, 1
        # 여기도 interval 순서는 뒤죽박죽...
        intervals.sort(key=lambda interval: interval[END])
        
        last_end = float("-inf")
        answer = 0
        for interval in intervals:
            if last_end > interval[START]:
                # last_end가 갱신되는 경우. 여기선 min을 볼 필요가 없음.
                answer += 1
            else:
                # 겹치지 않는 경우엔 아니면 last_end를 업데이트해준다.
                last_end = interval[END]
                
        return answer