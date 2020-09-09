class Solution:
    def compareVersion(self, version1, version2):
        a1 = version1.split('.')
        a2 = version2.split('.')
        for i in range(max(len(a1), len(a2))):
            t1 = 0
            if i < len(a1):
                t1 = int(a1[i])

            t2 = 0
            if i < len(a2):
                t2 = int(a2[i])
            if t1 < t2:
                return -1
            if t1 > t2:
                return 1
        return 0
