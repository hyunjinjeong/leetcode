class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 시작점을 기준으로 정렬
        intervals.sort(key=lambda interval: interval[0])
        
        left = []
        merged = intervals[0]
        for start, end in intervals:
            prev_start, prev_end = merged
            
            if start <= prev_end:
                merged = [prev_start, max(prev_end, end)]
            else:
                left.append(merged)
                merged = [start, end]
            
        return left + [merged]