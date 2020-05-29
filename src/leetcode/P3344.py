class Solution:
    def canFinish(self, numCourses, prerequisites):
        map = {}
        for i in range(numCourses):
            map[i] = []
        for pair in prerequisites:
            map[pair[0]].append(pair[1])
        learned = [False] * numCourses
        for i in range(numCourses):
            found = False
            for j in range(numCourses):
                if not learned[j] and len(map[j]) == 0:
                    found = True
                    learned[j] = True
                    for k in range(numCourses):
                        if not learned[k] and j in map[k]:
                            map[k].remove(j)
                    break
            if not found:
                return False
        return True


if __name__ == '__main__':
    print(Solution().canFinish(2, [[1, 0]]))
