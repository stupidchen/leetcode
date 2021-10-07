from collections import defaultdict
from typing import List

START = 'JFK'


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        sub = defaultdict(lambda: [])
        for ticket in tickets:
            s, t = ticket
            sub[s].append(t)
        for s in sub:
            sub[s].sort()
        n = len(tickets)
        visit = {}
        for s in sub:
            visit[s] = [False] * len(sub[s])

        it = [START]

        def find(cur, num):
            if num == n:
                return it

            for i, t in enumerate(sub[cur]):
                if not visit[cur][i]:
                    visit[cur][i] = True
                    it.append(t)
                    res = find(t, num + 1)
                    if res is not None:
                        return res
                    visit[cur][i] = False
                    it.pop()

        return find(START, 0)


if __name__ == '__main__':
    print(Solution().findItinerary([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]))
