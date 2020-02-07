class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        m = max(persons) + 1
        self.v = [0] * m
        self.t = []
        self.s = min(persons)
        max_c = 0
        max_t = min(persons)
        for i in range(len(persons)):
            self.v[persons[i]] += 1
            if self.v[persons[i]] >= max_c:
                max_t = persons[i]
                max_c = self.v[persons[i]]
            self.t.append(max_t)
        self.n = len(times)
        self.times = times

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        l = 0
        r = self.n
        while r - l > 1:
            mid = (l + r) >> 1
            if t >= self.times[mid]:
                l = mid
            else:
                r = mid
        if l >= self.n:
            l = self.n - 1
        return self.t[l]


if __name__ == '__main__':
    t = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    print(t.q(3))
    print(t.q(12))
    print(t.q(25))
    print(t.q(15))
    print(t.q(24))
    print(t.q(8))
