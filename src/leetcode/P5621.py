class Solution:
    def countStudents(self, students, sandwiches):
        n = len(students)
        m = len(sandwiches)
        v = [False] * n
        l = -1
        i = 0
        t = 0
        while i != l:
            if not v[i]:
                if students[i] == sandwiches[t]:
                    v[i] = True
                    t += 1
                    l = i
                    if t == m:
                        return 0
            i = (i + 1) % n

        r = 0
        for i in range(n):
            if not v[i]:
                r += 1
        return r


if __name__ == '__main__':
    print(Solution().countStudents(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]))
