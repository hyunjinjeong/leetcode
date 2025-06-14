class MyCalendarTwo:
    # line sweep 이라는게 있네
    def __init__(self):
        # self.bookings = []
        # self.overlap_bookings = []
        self.events = collections.defaultdict(int)

    def book(self, startTime: int, endTime: int) -> bool:
        # for s1, e1 in self.overlap_bookings:
        #     if self.does_overlap(s1, e1, startTime, endTime):
        #         return False
        
        # for s1, e1 in self.bookings:
        #     if self.does_overlap(s1, e1, startTime, endTime):
        #         self.overlap_bookings.append((max(s1, startTime), min(e1, endTime)))

        # self.bookings.append((startTime, endTime))
        # return True
        self.events[startTime] += 1
        self.events[endTime] -= 1

        count = 0
        for event in sorted(self.events):
            count += self.events[event]
            if count > 2:
                self.events[startTime] -= 1
                self.events[endTime] += 1
                return False
        
        return True
    
    # def does_overlap(self, s1, e1, s2, e2):
    #     return max(s1, s2) < min(e1, e2)

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
