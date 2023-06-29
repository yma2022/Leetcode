class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        # print(self.calendar)
        self.calendar.sort(key = lambda x: x[1])
        left, right = 0, len(self.calendar)
        while left < right:
            mid = (left + right) // 2
            if self.calendar[mid][1] <= start:
                left = mid + 1
            elif self.calendar[mid][0] >= end:
                right = mid
            else:
                return False
        self.calendar.append([start, end])        
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)