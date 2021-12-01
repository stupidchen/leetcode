from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        length = 0
        for num in s:
            value = widths[ord(num) - 97]
            if (length + value) > 100:
                length = value
                lines += 1
            else:
                length += value
        return [lines, length]
