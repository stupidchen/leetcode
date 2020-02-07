class Solution:
    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        m = days[-1] + 20
        f = [0x7fffffff] * m
        for i in range(days[0]):
            f[i] = 0
        tickets = [1, 7, 30]
        k = -1
        for i in range(days[0], m):
            if k < len(days) - 1 and days[k + 1] == i:
                k += 1
            else:
                f[i] = f[i - 1]

            for j in range(3):
                t = tickets[j]
                if i - t + 1 <= days[k]:
                    if i - t <= 0:
                        last = 0
                    else:
                        last = f[i - t]
                    f[i] = min(f[i], last + costs[j])

        return min(f[days[-1]:])


if __name__ == '__main__':
    print(Solution().mincostTickets([1, 20, 41], [2, 7, 13]))
