from collections import Counter


class Solution:
    def minimizeStringValue(self, s: str) -> str:
        counter = Counter(s)
        if '?' in counter:
            del counter['?']
        for i in range(26):
            if (char := chr(ord('a') + i)) not in counter:
                counter[char] = 0

        si = list(s)
        pc = []
        for i, c in enumerate(si):
            if c != '?':
                continue

            mf = min(counter.values())
            for mc in range(26):
                if counter[(char := chr(ord('a') + mc))] == mf:
                    break

            pc.append(char)
            counter[char] += 1

        pc.sort()
        j = 0
        for i, c in enumerate(si):
            if c == '?':
                si[i] = pc[j]
                j += 1

        res = ''.join(si)
        return res


if __name__ == '__main__':
    r = Solution().minimizeStringValue("abcdefghijklmnopqrstuvwxy??")
    print(r)
