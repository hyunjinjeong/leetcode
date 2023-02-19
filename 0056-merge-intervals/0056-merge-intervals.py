class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 시작점을 기준으로 정렬
        intervals.sort(key=lambda interval: interval[0])
        
        left = []
        merged = intervals[0]
        for start, end in intervals:
            prev_start, prev_end = merged
            
            # 합쳐야 하는 상황
            if start <= prev_end:
                merged = [prev_start, max(prev_end, end)]
            # 안 합쳐도 되면 left 배열에 추가해주고.. merged를 갱신해줌
            else:
                left.append(merged)
                merged = [start, end]
            
        return left + [merged]