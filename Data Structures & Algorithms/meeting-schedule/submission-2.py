"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i : i.start)

        for i in range(len(intervals) - 1):
            firstMeeting = intervals[i]
            secondMeeting = intervals[i + 1]

            if firstMeeting.end > secondMeeting.start:
                return False

        return True