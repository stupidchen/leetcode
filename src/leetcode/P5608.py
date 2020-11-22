class Solution:
    def minimumEffort(self, tasks):
        n = len(tasks)
        tasks = sorted(tasks, key=lambda x: (x[1] - x[0], x[1], -x[0]))
        ret = 0
        s = 0
        t = 0
        for i in range(n):
            s += tasks[i][0]
            t = max(tasks[i][1], tasks[i][0] + t)
            ret = max(s, t)

        return ret


if __name__ == '__main__':
    print(Solution().minimumEffort(tasks=[[1, 3], [2, 4], [10, 11], [10, 12], [8, 9]]))
    print(Solution().minimumEffort([[1, 2], [2, 4], [4, 8]]))
    print(Solution().minimumEffort(tasks=[[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]))
