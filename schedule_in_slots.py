from datetime import datetime, timedelta
from typing import List, Tuple


class Solution:

    def find_free_time_slots(self, meetings_1: List[Tuple[str, str]], meetings_2: List[Tuple[str, str]]):
        """
        You are given two arrays that represent the schedules of two people.
        Each array consists of pairs of strings representing the start and end times of meetings on their calendars.
        Your task is to find the free time slots on both calendars.
        These free slots should be at least 30 minutes long, and they should not overlap with any meetings.
        The working hours are from 9:00 to 19:30.
        The input arrays may not be sorted and you should ignore any meetings that last the entire day. Note that the timezone difference has been normalized to UTC.

        TODO Below can be generalized if we instead merge all the arrays into one and then process a single sorted list. This reduces variable count and simplifies the comparisons.
        """

        def parse(s: str) -> datetime.time:
            return datetime.strptime(s, '%H:%M')

        def format_to_str(s: datetime) -> str:
            return datetime.strftime(s, '%H:%M')

        def parse_array(arr: List[Tuple[str, str]]):
            return [(parse(interval1[0]), parse(interval1[1])) for interval1 in arr]

        last_dummy = ('17:30', '18:00')
        meetings_1.append(last_dummy)
        meetings_2.append(last_dummy)

        meetings_1 = parse_array(meetings_1)
        meetings_2 = parse_array(meetings_2)

        meetings_1.sort()
        meetings_2.sort()

        current_time = parse("9:00")

        free_slots = []

        while meetings_1 and meetings_2:
            interval1 = meetings_1[0]
            interval2 = meetings_2[0]

            next_meeting_start = min(interval1[0], interval2[0])
            if next_meeting_start - current_time >= timedelta(minutes=30):
                free_slots.append((current_time, next_meeting_start))

            if interval1[0] <= interval2[0] < interval1[1] or interval2[0] <= interval1[0] < interval2[1]:
                # overlap
                next_free_time_start = max(interval1[1], interval2[1])
                meetings_1.pop(0)
                meetings_2.pop(0)

            else:
                # not overlap discard only the first
                next_free_time_start = min(interval1[1], interval2[1])
                if interval1[1] == next_free_time_start:
                    meetings_1.pop(0)

                else:
                    meetings_2.pop(0)

            current_time = next_free_time_start

        result = [(format_to_str(interval[0]), format_to_str(interval[1])) for interval in free_slots]
        print(result)
        return result


assert Solution().find_free_time_slots(
    [("11:00", "12:30"), ("13:30", "15:30"), ("15:30", "16:00"), ("17:00", "18:00")],
    [("10:00", "11:30"), ("13:00", "14:00"), ("17:00", "19:00")]
) == [('09:00', '10:00'), ("12:30", "13:00"), ("16:00", "17:00")]