class Solution:
    def minFlips(self, target: str) -> int:
        r = 0
        n = len(target)
        i = 0
        while i < n:
            j = i
            while j < n and target[j] == str(r & 1):
                j += 1
            if j < n:
                r += 1
            i = j
        return r


if __name__ == '__main__':
    print(Solution().minFlips('101'))
    print(Solution().minFlips('000'))
