##Insert Interval
##Given a set of non-overlapping intervals,
##insert a new interval into the intervals (merge if necessary).
##You may assume that the intervals were initially sorted according to
##their start times.
##
##2015年7月6日   AC
##zss

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        flag = True
        while flag:
            flag = False
            for interval in intervals:
                if (newInterval.end-newInterval.start)+(interval.end-interval.start)>=max(newInterval.end,interval.end)-min(newInterval.start,interval.start):
                    intervals.remove(interval)
                    newInterval.start = min(newInterval.start,interval.start)
                    newInterval.end = max(newInterval.end,interval.end)
                    flag = True
                    break
        intervals.append(newInterval)
        intervals.sort(key= lambda x:x.start)
        return intervals

##class Test:
##    def t(self):
##        i1 = Interval(1,2)
##        i2 = Interval(3,5)
##        i3 = Interval(6,7)
##        i4 = Interval(8,10)
##        i5 = Interval(12,16)
##        i = Interval(4,9)
##        return[i1,i2,i3,i4,i5],i
