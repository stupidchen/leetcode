from collections import Counter
from typing import List


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        counter = Counter()
        for s in arr:
            for length in range(1, len(s) + 1):
                seen = set()
                for i in range(len(s) - length + 1):
                    substr = s[i:i + length]
                    if substr not in seen:
                        counter[substr] += 1
                        seen.add(substr)

        res = [0] * len(arr)
        for i, s in enumerate(arr):
            answer = ''
            for length in range(1, len(s) + 1):
                for j in range(len(s) - length + 1):
                    substr = s[j:j + length]
                    if counter[substr] == 1:
                        if answer:
                            if answer > substr:
                                answer = substr
                        else:
                            answer = substr
                if answer:
                    break
            res[i] = answer
        return res


if __name__ == '__main__':
    r = Solution().shortestSubstrings(arr=["gfnt", "xn", "mdz", "yfmr", "fi", "wwncn", "hkdy"])
    print(r)
