class SummaryRanges:

    def __init__(self):
        self.numbers = set()

    def addNum(self, value: int) -> None:
        self.numbers.add(value)

    def getIntervals(self) -> List[List[int]]:
        intervals = []
        for num in sorted(self.numbers):
            if intervals and intervals[-1][1] == num - 1:
                intervals[-1][1] = num
            else:
                intervals.append([num, num])

        return intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()