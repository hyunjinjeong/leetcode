class SummaryRanges:
    # disjoint interval이 뭔 소리지
    # 1 -> 1 1
    # 3 -> 1 1 / 3 3
    # 7 -> 1 1 / 3 3 / 7 7
    # 2 -> 1 3 / 7 7
    # 6 -> 1 3 / 6 7    <-- 여기 왜 6 6 / 7 7 이 아니고 6 7인 거지? 연속된 숫자는 하나의 interval에 들어가야 하는 듯
    # 새 숫자가 추가되면 범위를 나눠야 하는 듯?
    # 근데 병합은 어케 하지? brute force로 일단 해보자

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        self.intervals.append([value, value])

    def getIntervals(self) -> List[List[int]]:
        if not self.intervals:
            return self.intervals

        self._merge_intervals()
        return self.intervals
    
    def _merge_intervals(self):
        self.intervals.sort(key=lambda pair: pair[0])
        
        new_intervals = [[self.intervals[0][0], self.intervals[0][1]]]
        for i in range(1, len(self.intervals)):
            start, end = self.intervals[i]
            prev_start, prev_end = new_intervals[-1]

            if prev_end + 1 == start or prev_end == start or prev_start + 1 == start or prev_start == start:
                new_intervals[-1] = [prev_start, max(end, prev_end)]
            else:
                new_intervals.append([start, end])
        
        self.intervals = new_intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()