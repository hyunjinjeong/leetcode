class MyCalendar:

    def __init__(self):
        self.events = sortedcontainers.SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        self.events[startTime] = self.events.get(startTime, 0) + 1
        self.events[endTime] = self.events.get(endTime, 0) - 1

        count = 0
        for event in self.events:
            count += self.events[event]
            if count > 1:
                self.events[startTime] -= 1
                self.events[endTime] += 1
                return False

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
