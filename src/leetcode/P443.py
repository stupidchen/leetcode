from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        chars += '^'
        last = 0
        r = ''
        for i in range(1, len(chars)):
            if chars[i] != chars[i - 1]:
                if i - last == 1:
                    r += chars[i - 1]
                else:
                    r += chars[i - 1] + str(i - last)
                last = i
        for i in range(len(r)):
            chars[i] = r[i]
        return len(r)


if __name__ == '__main__':
    print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))
