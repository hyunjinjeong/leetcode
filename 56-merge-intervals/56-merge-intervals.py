class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         answer = []
        
#         # interval은 정렬 안 되어 있고 순서가 뒤죽박죽
#         intervals.sort(key=lambda interval: interval[0])
        
#         curr_start, curr_end = intervals[0]
#         for start, end in intervals:
#             # 안 겹치는 경우
#             if start > curr_end:
#                 answer.append([curr_start, curr_end])
#                 curr_start, curr_end = start, end
#             else:
#                 # end는 정렬 안 되어 있으니까 max를 골라야 함.
#                 curr_end = max(curr_end, end)
        
#         # 마지막은 안 더해졌으니까 추가..
#         answer.append([curr_start, curr_end])
        
#         return answer

        # 이건 Solution인데 이렇게 하면 좀 더 코드가 깔끔함!
        START, END = 0, 1
        answer = []
        
        intervals.sort(key=lambda interval: interval[0])
        for interval in intervals:
            if not answer or interval[START] > answer[-1][END]:
                answer.append(interval)
            else:
                answer[-1][END] = max(interval[END], answer[-1][END])
        
        return answer