class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), k << 1):
            s[i: i + k] = list(reversed(s[i: i + k]))
        return ''.join(s)
