##Gas Station
##There are N gas stations along a circular route,
##where the amount of gas at station i is gas[i].
##You have a car with an unlimited gas tank and it costs cost[i]
##of gas to travel from station i to its next station (i+1).
##You begin the journey with an empty tank at one of the gas stations.
##
##Return the starting gas station's index if you can travel
##around the circuit once, otherwise return -1.
##
##2015年8月17日 16:28:03  AC
##zss

##若从i开始 到j站时 tank<0 则必然有从i+1到j tank<0
##因此直接到j+1进行尝试即可


class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        c = len(gas)
        if c == 0: return -1
        left = [gas[i]-cost[i] for i in range(c)]
        if sum(left)<0:return -1
        start = tank = i = 0
        while i<c:
            if(tank<0):
                tank = left[i]
                start=i
            else:
                tank += left[i]
            i+=1
        return start
