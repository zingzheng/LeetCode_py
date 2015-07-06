##Merge Intervals
##Given a collection of intervals, merge all overlapping intervals.
##
##2015年7月6日  AC
##zss


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        results = []
        for interval in intervals:
            flag = True
            while flag:
                flag = False
                for result in results:
                    if (interval.end-interval.start)+(result.end-result.start)>=max(interval.end,result.end)-min(interval.start,result.start):
                        results.remove(result)
                        interval.start = min(interval.start,result.start)
                        interval.end = max(interval.end,result.end)
                        flag = True
                        break
            results.append(interval)
        return results

##class Test:
##    def t(self):
##        i1 = Interval(1,3)
##        i2 = Interval(2,6)
##        i3 = Interval(8,10)
##        i4 = Interval(15,18)
##        return[i1,i2,i3,i4]
