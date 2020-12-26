class Solution:
    def averageWaitingTime(self, customers):
        n = len(customers)
        t = -1
        ret = 0
        for i in range(n):
            l, r = customers[i]
            if l >= t:
                t = l + r
            else:
                ret += t - l
                t = t + r
            ret += r
        return ret / n


if __name__ == '__main__':
    print(Solution().averageWaitingTime([[1, 2], [2, 5], [4, 3]]))
