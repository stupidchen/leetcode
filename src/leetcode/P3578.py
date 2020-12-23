class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = str(n)
        l = len(s)
        for i in reversed(range(l)):
            t = -1
            for j in reversed(range(i + 1, l)):
                if s[i] < s[j]:
                    t = j
                    break
            if t != -1:
                r = int(s[:i] + s[t] + ''.join(list(sorted(s[i+1:t] + s[i] + s[t+1:]))))
                if r <= (1 << 31) - 1:
                    return int(s[:i] + s[t] + ''.join(list(sorted(s[i+1:t] + s[i] + s[t+1:]))))
        return -1


if __name__ == '__main__':
    print(Solution().nextGreaterElement(12))
