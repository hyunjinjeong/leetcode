class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # 겹치는 interval이 없어야 함
        # 정렬한 뒤에 보면 되지 않나?
        START, END = 0, 1
        
        intervals.sort()
        for i in range(1, len(intervals)):
            prev, curr = intervals[i-1], intervals[i]
            
            if curr[START] < prev[END]:
                return False
        
        return True