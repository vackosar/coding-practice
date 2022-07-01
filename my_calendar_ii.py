# https://leetcode.com/problems/my-calendar-ii/submissions/
class MyCalendarTwo:
    """
    Return false if 3-ple booking detected and not adding the event.
    Non zero interval if event1.intersect(event2) is non zero.
    That is when max(event1.start, event2.start) < min(event1.end, event2.end).

    I could store over laps, then I just need to overlap those.
    In that case the slowest is the linear solution, where i then search check all the intervals.
    There may be some method

    """

    def __init__(self):
        self.events = []
        self.double_booked = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.double_booked:
            if max(start, s) < min(end, e):
                return False

        for s, e in self.events:
            if max(start, s) < min(end, e):
                os = max(start, s)
                oe = min(end, e)
                self.double_booked.append((os, oe))

        self.events.append((start, end))
        self.events.sort()
        self.double_booked.sort()
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
