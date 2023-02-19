class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         # 시작점을 기준으로 정렬
#         intervals.sort(key=lambda interval: interval[0])
        
#         left = []
#         merged = intervals[0]
#         for start, end in intervals:
#             prev_start, prev_end = merged
            
#             # 합쳐야 하는 상황
#             if start <= prev_end:
#                 merged = [prev_start, max(prev_end, end)]
#             # 안 합쳐도 되면 left 배열에 추가해주고.. merged를 갱신해줌
#             else:
#                 left.append(merged)
#                 merged = [start, end]
            
#         return left + [merged]
    
        # 이건 Solution인데 이렇게 하면 좀 더 코드가 깔끔함!
        # answer에 넣어두고 answer[-1]의 원소를 갱신하는 방법.
        START, END = 0, 1
        answer = []
        
        intervals.sort(key=lambda interval: interval[0])
        for interval in intervals:
            if not answer or interval[START] > answer[-1][END]:
                answer.append(interval)
            else:
                answer[-1][END] = max(interval[END], answer[-1][END])
        
        return answer