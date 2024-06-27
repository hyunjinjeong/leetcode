class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # start, end
        # end로 정렬하면?
        # 14 36 28
        # 뒤에 있는데, start가 앞에 있는 interval들과 같거나 작은게 있으면 됨.
        # 그.. monotonic increasing stack 쓰면 되지 않으려나
        # while stack[-1] >= start
        # 아 문제는 end가 같을 때 start가 역순으로 정렬되어 있어야 함.

        intervals.sort(key=lambda interval: (interval[1], -interval[0]))
        stack = []

        for start, end in intervals:
            while stack and stack[-1] >= start:
                stack.pop()
            stack.append(start)
        
        return len(stack)