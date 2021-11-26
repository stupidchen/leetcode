import bisect
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = bisect.bisect_right(letters, target)
        if i >= len(letters):
            i = 0
        return letters[i]


if __name__ == '__main__':
    print(Solution().nextGreatestLetter(letters=["c", "f", "j"], target="j"))
