from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        c = 0
        r = 0
        while tickets[k] != 0:
            while tickets[c] == 0:
                c = (c + 1) % n
            tickets[c] -= 1
            c = (c + 1) % n
            r += 1
        return r


if __name__ == '__main__':
    print(Solution().timeRequiredToBuy(tickets=[2, 3, 2], k=2))
