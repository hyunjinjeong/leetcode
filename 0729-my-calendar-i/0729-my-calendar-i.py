class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        for booking in self.bookings:
            b1, b2 = sorted([booking, (startTime, endTime)])
            if b1[1] > b2[0]:
                return False
        
        self.bookings.append((startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)