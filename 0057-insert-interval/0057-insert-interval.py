class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 어렵게 생각했는데 구현 문제에 가까움..
        # 왼쪽, 오른쪽에 각각 추가하고, 중간에 들어갈 것들은 인덱스를 추적.
        left, right = [], []
        mid_start, mid_end = newInterval
        
        for interval in intervals:
            # 안 겹치는 경우엔 현재 interval을 각각 왼쪽, 오른쪽에 추가하면 됨
            if interval[0] > mid_end:
                right.append(interval)
            elif interval[1] < mid_start:
                left.append(interval)
            else:
                # 겹치는 경우엔 merge. mid_start, mid_end를 구해줘야 한다.
                mid_start = min(mid_start, interval[0])
                mid_end = max(mid_end, interval[1])
        
        return left + [[mid_start, mid_end]] + right
                
                
            