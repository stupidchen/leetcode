class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        s = 0
        m = 0
        p = -1
        for i in range(n):
            s += gas[i] - cost[i]
            if s < m:
                m = s
                p = i

        if s >= 0:
            return (p + 1) % n
        return -1