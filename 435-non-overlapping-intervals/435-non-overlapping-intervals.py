class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        START, END = 0, 1
        # 여기도 interval 순서는 뒤죽박죽...
        intervals.sort(key=lambda interval: interval[START])
        
        # last_end를 저장해두고 overlap을 만날 때마다 +1 해주면 됨.
        last_end = intervals[0][END]
        answer = 0
        # 이 때는 첫 요소는 빼야 함
        for interval in intervals[1:]:
            # last_end가 갱신되어야 하는 경우
            if last_end > interval[START]:
                # last_end가 갱신되는 경우.
                answer += 1
                # END가 더 큰거를 없애야 함. 뒤에 영향이 안 가게..
                last_end = min(last_end, interval[END])
            else:
                # 겹치지 않는 경우엔 아니면 last_end를 업데이트해준다.
                last_end = interval[END]
                
        return answer