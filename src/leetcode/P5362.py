from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        d = Counter(s)
        t = 0
        for i in d.values():
            if i & 1 == 1:
                t += 1
        if t > k:
            return False
        return True


if __name__ == '__main__':
    print(Solution().canConstruct('leetcode', 3))
    print(Solution().canConstruct(s="annabelle", k=2))
    print(Solution().canConstruct(s="truee", k=3))
