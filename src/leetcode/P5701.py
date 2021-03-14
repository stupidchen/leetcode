class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        for i in range(len(s1)):
            for j in range(i):
                t = s1[:j] + s1[i] + s1[j + 1:i] + s1[j] + s1[i + 1:]
                if t == s2:
                    return True
        return False

if __name__ == '__main__':
    print(Solution().areAlmostEqual('abcd', 'abcd'))
